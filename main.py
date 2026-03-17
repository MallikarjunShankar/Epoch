from simulation.simulation_engine import initialize_simulation, simulation_step
from config import CONFIG
from visualization.visualizer import Visualizer


def main():
    sim_state = initialize_simulation(CONFIG)

    # ✅ Pass world, not config
    visualizer = Visualizer(sim_state["world"])

    def state_provider():
        nonlocal sim_state
        sim_state = simulation_step(sim_state, CONFIG)

        # TEMP structure to satisfy visualizer
        return {
            "world": sim_state["world"],
            "agents": [],        # Stage 1 will fill this
            "alliances": [],
            "trades": [],
            "conflicts": [],
            "stats": {}
        }

    visualizer.run(state_provider)


if __name__ == "__main__":
    main()