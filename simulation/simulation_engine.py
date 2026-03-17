from simulation.resource_system import spawn_resources, decay_resources
from agents.memory.agent_memory import (
    update_direction_success,
    decay_direction,
    mutate_direction
)
from agents.agent import create_agent, update_energy, is_dead
from agents.movement import random_movement, move_towards, biased_movement
from agents.perception import find_nearest_resource
from agents.consumption import consume_resource


def initialize_simulation(config):
    world = {
        "width": config["world_width"],
        "height": config["world_height"],
        "resources": []
    }

    agents = []
    for i in range(config["initial_agent_count"]):
        agents.append(create_agent(i, world))

    simulation_state = {
        "world": world,
        "agents": agents,
        "alliances": [],
        "trades": [],
        "conflicts": [],
        "stats": {},
        "tick": 0
    }

    return simulation_state


def simulation_step(simulation_state, config):
    world = simulation_state["world"]
    agents = simulation_state["agents"]

    spawn_resources(
        world,
        spawn_rate=config["resource_spawn_rate"],
        max_amount=config["resource_max_amount"]
    )

    decay_resources(
        world,
        decay_rate=config["resource_decay_rate"]
    )

    alive_agents = []
    new_agents = []

    for agent in agents:
        resource = find_nearest_resource(
            agent,
            world,
            vision_radius=config["vision_radius"]
        )

        if resource:
            move_towards(agent, resource["position"], world)
            update_direction_success(agent, resource["position"])

            if agent["position"] == resource["position"]:
                consume_resource(
                    agent,
                    world,
                    resource["index"],
                    config["consumption_rate"]
                )
        else:
            biased_movement(agent, world)
            decay_direction(agent)

        update_energy(agent, config["energy_decay"])

        if agent["energy"] > config.get("reproduction_threshold", 120):
            child = agent.copy()
            child["id"] = config.get("next_agent_id", 1000)
            config["next_agent_id"] = config.get("next_agent_id", 1000) + 1
            child["energy"] *= 0.5
            child["memory"]["food_direction"] = mutate_direction(
                agent["memory"]["food_direction"]
            )
            new_agents.append(child)

        if not is_dead(agent):
            alive_agents.append(agent)

    simulation_state["agents"] = alive_agents + new_agents
    simulation_state["tick"] += 1

    return simulation_state