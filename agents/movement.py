import random

def random_movement(agent, world, step_size = 1):
    x, y = agent["position"]

    dx = random.randint(-step_size, step_size)
    dy = random.randint(-step_size, step_size)

    new_x = max(0, min(world["width"] - 1, x + dx))
    new_y = max(0, min(world["height"] - 1, y + dy))

    agent["position"] = (new_x, new_y)