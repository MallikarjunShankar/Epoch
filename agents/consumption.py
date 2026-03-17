def consume_resource(agent, world, resource_index, consumption_rate = 5):
    x, y, amount = world["resources"][resource_index]
    consumed = min(amount, consumption_rate)
    agent["energy"] += consumed
    remaining = amount - consumed

    if remaining <= 0:
        world["resources"].pop(resource_index)
    else:
        world["resources"][resource_index] = (x, y, remaining)
        