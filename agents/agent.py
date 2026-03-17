import random

def create_agent(agent_id, world):
    x = random.randint(0, world["width"] - 1)
    y = random.randint(0, world["height"] - 1)

    return {
        "id": agent_id,
        "position": (x, y),
        "energy": random.uniform(50, 100),
        "inventory": {"food": 0},
        "memory": {},
        "trust_scores": {},
        "faction": None,
        "state": "neutral"
    }

def update_energy(agent, decay = 0.5):
    agent["energy"] -= decay

def is_dead(agent):
    return agent["energy"] <= 0

