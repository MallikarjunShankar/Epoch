import random

def create_world(width, height):
    return {
        "width" : width,
        "height" : height,
        "resources" : []
    }

def add_resource(world, x, y, amount):
    world["resources"].append((x, y, amount))

def remove_resource(world, index):
    if 0 <= index < len(world["resources"]):
        world["resources"].pop(index)

def get_resources(world):
    return world["resources"]