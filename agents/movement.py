import random

def random_movement(agent, world, step_size = 1):
    x, y = agent["position"]

    dx = random.randint(-step_size, step_size)
    dy = random.randint(-step_size, step_size)

    new_x = max(0, min(world["width"] - 1, x + dx))
    new_y = max(0, min(world["height"] - 1, y + dy))

    agent["position"] = (new_x, new_y)

def move_towards(agent, target_pos, world):
    ax, ay = agent["position"]
    tx, ty = target_pos
    
    dx = tx - ax
    dy = ty - ay

    step_x = 0 if dx == 0 else int(dx / abs(dx))
    step_y = 0 if dy == 0 else int(dy / abs(dy))

    new_x = max(0, min(world["width"] - 1, ax + step_x))
    new_y = max(0, min(world["height"] - 1, ay + step_y))

    agent["position"] = (new_x, new_y)

def biased_movement(agent, world):
    x, y = agent["position"]
    dx_bias, dy_bias = agent["memory"]["food_direction"]

    dx = random.choice([-1, 0, 1]) + dx_bias
    dy = random.choice([-1, 0, 1]) + dy_bias

    step_x = int(max(-1, min(1, dx)))
    step_y = int(max(-1, min(1, dy)))

    new_x = max(0, min(world["width"] - 1, x + step_x))
    new_y = max(0, min(world["height"] - 1, y + step_y))

    agent["position"] = (new_x, new_y)