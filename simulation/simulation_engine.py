from simulation.resource_system import spawn_resources, decay_resources

def initialize_simulation(config):
    world = {
        "width": config["world_width"],
        "height": config["world_height"],
        "resources": []
    }

    simulation_state = {
        "world": world,
        "tick": 0
    }

    return simulation_state

def simulation_step(simulation_state, config):
    world = simulation_state["world"]

    spawn_resources(
        world,
        spawn_rate=config["resource_spawn_rate"],
        max_amount=config["resource_max_amount"]
    )

    decay_resources(
        world,
        decay_rate=config["resource_decay_rate"]
    )

    simulation_state["tick"] += 1
    
    return simulation_state