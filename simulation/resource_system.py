import random

MAX_RESOURCES = 700
PRUNE_BATCH = 50


def spawn_resources(world, spawn_rate=5, max_amount=20):
    for _ in range(spawn_rate):
        if world["resources"] and random.random() < 0.7:
            rx, ry, _ = random.choice(world["resources"])
            x = rx + random.randint(-10, 10)
            y = ry + random.randint(-10, 10)
        else:
            x = random.randint(0, world["width"] - 1)
            y = random.randint(0, world["height"] - 1)

        x = max(0, min(world["width"] - 1, x))
        y = max(0, min(world["height"] - 1, y))

        amount = random.uniform(5, max_amount)
        world["resources"].append((x, y, amount))


def prune_resources(world, config):
    resources = world["resources"]
    max_resources = config.get("resource_max_count", MAX_RESOURCES)

    if len(resources) <= max_resources:
        return

    remove_count = min(PRUNE_BATCH, len(resources) - max_resources)

    for _ in range(remove_count):
        idx = random.randint(0, len(resources) - 1)
        resources[idx] = resources[-1]
        resources.pop()


def update_resources(world, config):
    spawn_resources(
        world,
        spawn_rate=config["resource_spawn_rate"],
        max_amount=config["resource_max_amount"]
    )

    prune_resources(world, config)