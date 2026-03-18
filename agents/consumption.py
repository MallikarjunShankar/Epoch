import random

def consume_nearest_and_update(agent, world, consumption_rate, max_distance=2):
    ax, ay = agent["position"]
    resources = world["resources"]

    if not resources:
        return False

    best_idx = None
    best_dist_sq = max_distance * max_distance

    for i, (x, y, amount) in enumerate(resources):
        dx = x - ax
        dy = y - ay
        dist_sq = dx * dx + dy * dy
        if dist_sq <= best_dist_sq:
            best_idx = i
            best_dist_sq = dist_sq

    if best_idx is None:
        return False

    x, y, amount = resources[best_idx]
    consumed = min(amount, consumption_rate)
    agent["energy"] += consumed

    remaining = amount - consumed
    if remaining <= 0:
        resources[best_idx] = resources[-1]
        resources.pop()
    else:
        resources[best_idx] = (x, y, remaining)

    return True

def consume_resource(agent, world, position, consumption_rate):
    for i, (x, y, amount) in enumerate(world["resources"]):
        if (x, y) == position:
            consumed = min(amount, consumption_rate)
            agent["energy"] += consumed

            remaining = amount - consumed
            if remaining <= 0:
                world["resources"].pop(i)
            else:
                world["resources"][i] = (x, y, remaining)
            return True
    return False