import random


def initialize_memory():
    return {
        "food_direction": (0.0, 0.0)
    }


def update_direction_success(agent, target_pos):
    ax, ay = agent["position"]
    tx, ty = target_pos

    dx = tx - ax
    dy = ty - ay

    if dx != 0:
        dx /= abs(dx)
    if dy != 0:
        dy /= abs(dy)

    old_dx, old_dy = agent["memory"]["food_direction"]

    new_dx = (old_dx * 0.8) + (dx * 0.2)
    new_dy = (old_dy * 0.8) + (dy * 0.2)

    agent["memory"]["food_direction"] = (new_dx, new_dy)


def decay_direction(agent, decay=0.95):
    dx, dy = agent["memory"]["food_direction"]

    agent["memory"]["food_direction"] = (
        dx * decay,
        dy * decay
    )


def mutate_direction(direction, mutation_strength=0.3):
    dx, dy = direction

    dx += random.uniform(-mutation_strength, mutation_strength)
    dy += random.uniform(-mutation_strength, mutation_strength)

    return (dx, dy)