import random
from agents.memory.agent_memory import initialize_memory


def create_agent(agent_id, world):
    x = random.randint(0, world["width"] - 1)
    y = random.randint(0, world["height"] - 1)

    base_memory = initialize_memory()

    return {
        "id": agent_id,
        "position": (x, y),
        "energy": random.uniform(50, 100),
        "inventory": {"food": 0},
        "memory": {
            **base_memory,
            "target": None,
            "target_cooldown": 0
        },
        "trust_scores": {},
        "faction": None,
        "state": "neutral"
    }


def update_energy(agent, decay):
    agent["energy"] -= decay


def is_dead(agent):
    return agent["energy"] <= 0