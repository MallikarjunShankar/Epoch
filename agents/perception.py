import random

MAX_CHECKS = 40


def find_nearest_resource(agent, world, vision_radius=80):
    ax, ay = agent["position"]
    resources = world["resources"]

    if not resources:
        return None

    best_pos = None
    best_dist = float("inf")

    checks = min(MAX_CHECKS, len(resources))

    for _ in range(checks):
        x, y, _ = resources[random.randint(0, len(resources) - 1)]

        dx = x - ax
        dy = y - ay
        dist = dx * dx + dy * dy

        if dist < vision_radius * vision_radius and dist < best_dist:
            best_dist = dist
            best_pos = (x, y)

    return best_pos