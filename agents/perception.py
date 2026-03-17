import math

def find_nearest_resource(agent, world, vision_radius = 50):
    ax, ay = agent["position"]
    closest = None
    min_dist = float("inf")

    for i, (x, y, amount) in enumerate(world["resources"]):
        dx = x - ax
        dy = y - ay
        dist = math.sqrt(dx * dx + dy * dy)

        if dist < vision_radius and dist < min_dist:
            min_dist = dist
            closest = {
                "index": i,
                "position": (x, y),
                "amount": amount
            }

    return closest