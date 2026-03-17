from simulation.resource_system import spawn_resources, decay_resources
from agents.agent import create_agent, update_energy, is_dead
from agents.movement import random_movement

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

    for agent in agents:
        random_movement(agent, world)
        update_energy(agent, config["energy_decay"])

        if not is_dead(agent):
            alive_agents.append(agent)

    simulation_state["tick"] += 1
    
    return simulation_state