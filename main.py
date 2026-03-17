from simulation.simulation_engine import initialize_simulation, simulation_step
from config import CONFIG
from visualization.visualizer import Visualizer


def main():
    sim_state = initialize_simulation(CONFIG)

    visualizer = Visualizer(sim_state["world"])

    def state_provider():
        nonlocal sim_state

        sim_state = simulation_step(sim_state, CONFIG)
        print("Agents:", len(sim_state["agents"]))
        
        return {
            "world": sim_state["world"],
            "agents": sim_state["agents"],
            "alliances": sim_state["alliances"],
            "trades": sim_state["trades"],
            "conflicts": sim_state["conflicts"],
            "stats": sim_state["stats"]
        }

    visualizer.run(state_provider)

if __name__ == "__main__":
    main()