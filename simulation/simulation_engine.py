from simulation.resource_system import update_resources

from agents.agent import create_agent, update_energy, is_dead
from agents.movement import move_towards, biased_movement
from agents.perception import find_nearest_resource
from agents.consumption import consume_nearest_and_update

from agents.memory.agent_memory import (
    update_direction_success,
    decay_direction,
    mutate_direction
)


def initialize_simulation(config):
    world = {
        "width": config["world_width"],
        "height": config["world_height"],
        "resources": []
    }

    agents = []
    for i in range(config["initial_agent_count"]):
        agents.append(create_agent(i, world))

    return {
        "world": world,
        "agents": agents,
        "alliances": [],
        "trades": [],
        "conflicts": [],
        "stats": {},
        "tick": 0
    }


def simulation_step(simulation_state, config):
    world = simulation_state["world"]
    agents = simulation_state["agents"]

    update_resources(world, config)

    alive_agents = []
    new_agents = []

    tick = simulation_state["tick"]

    for i, agent in enumerate(agents):
        target = agent["memory"].get("target")
        cooldown = agent["memory"].get("target_cooldown", 0)

        if cooldown > 0:
            agent["memory"]["target_cooldown"] -= 1
        else:
            target = find_nearest_resource(
                agent,
                world,
                vision_radius=config["vision_radius"]
            )
            agent["memory"]["target"] = target
            agent["memory"]["target_cooldown"] = 5

        if target:
            move_towards(agent, target, world)
            update_direction_success(agent, target)
        else:
            biased_movement(agent, world)
            decay_direction(agent)

        consumed = consume_nearest_and_update(
            agent,
            world,
            config["consumption_rate"],
            max_distance=1
        )
        if consumed:
            stats = simulation_state.get("stats", {})
            stats["consumed"] = stats.get("consumed", 0) + 1
            simulation_state["stats"] = stats

        update_energy(agent, config["energy_decay"])

        if agent["energy"] > config["reproduction_threshold"]:
            max_agents = config.get("max_agents", 500)
            if len(alive_agents) + len(new_agents) < max_agents:
                # Spread reproduction across time and cost energy from parent.
                if agent["energy"] > config.get("reproduction_threshold", 150) + config.get("reproduction_cost", 80):
                    parent_energy = agent["energy"] - config.get("reproduction_cost", 80)
                    child_energy = parent_energy * 0.4
                    agent["energy"] = parent_energy * 0.6

                    child = {
                        **agent,
                        "id": config["next_agent_id"],
                        "energy": child_energy,
                        "memory": agent["memory"].copy()
                    }
                    config["next_agent_id"] += 1
                    child["memory"]["food_direction"] = mutate_direction(
                        agent["memory"]["food_direction"]
                    )
                    child["memory"]["target"] = None
                    child["memory"]["target_cooldown"] = 0
                    new_agents.append(child)

        if not is_dead(agent):
            alive_agents.append(agent)

    simulation_state["agents"] = alive_agents + new_agents
    simulation_state["tick"] += 1

    return simulation_state