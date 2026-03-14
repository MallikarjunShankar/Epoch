import pygame

BASE_RESOURCE_SIZE = 2
RESOURCE_COLOR_LOW = (40, 120, 40)
RESOURCE_COLOR_MED = (60, 180, 60)
RESOURCE_COLOR_HIGH = (100, 255, 100)

class ResourceRenderer:
    def __init__(self):
        pass

    def get_resource_color(self, amount):
        if amount < 10:
            return RESOURCE_COLOR_LOW
        elif amount < 25:
            return RESOURCE_COLOR_MED
        else:
            return RESOURCE_COLOR_HIGH
        
    def compute_size(self, amount, camera):
        base = BASE_RESOURCE_SIZE * camera.zoom * 0.3
        size = base + amount * 0.05
        return max(2, int(size))
    
    def draw_resource(self, screen, x, y, amount, camera):
        sx, sy = camera.world_to_screen((x,y))
        screen_w, screen_h = screen.get_size()

        if sx < -10 or sy < -10 or sx > screen_w + 10 or sy > screen_h + 10:
            return
        
        size = self.compute_size(amount, camera)
        color = self.get_resource_color(amount)

        pygame.draw.rect(
            screen,
            color, 
            (sx, sy, size, size)
        )

    def draw(self, screen, resources, camera):
        for x, y, amount in resources:
            self.draw_resource(
                screen,
                x,
                y,
                amount,
                camera
            )