import random

def spawn_resources(world, spawn_rate=5, max_amount=20):
    for _ in range(spawn_rate):
        x = random.randint(0, world["width"] - 1)
        y = random.randint(0, world["height"] - 1)
        amount = random.uniform(5, max_amount)

        world["resources"].append((x, y, amount))


def decay_resources(world, decay_rate=0.01):
    new_resources = []
    for (x, y, amount) in world["resources"]:
        amount *= (1 - decay_rate)
        if amount > 0.5:
            new_resources.append((x, y, amount))
    world["resources"] = new_resources