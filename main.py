from simulation.simulation_engine import initialize_simulation, simulation_step
from config import CONFIG
from visualization.visualizer import Visualizer


def main():
    sim_state = initialize_simulation(CONFIG)

    visualizer = Visualizer(sim_state["world"])

    def state_provider():
        nonlocal sim_state
        sim_state = simulation_step(sim_state, CONFIG)

        return {
            "world": sim_state["world"],
            "agents": sim_state["agents"],
            "alliances": [],
            "trades": [],
            "conflicts": [],
            "stats": {}
        }

    visualizer.run(state_provider)


if __name__ == "__main__":
    main()