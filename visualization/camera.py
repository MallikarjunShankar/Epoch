from dataclasses import dataclass

DEFAULT_ZOOM = 10.0
MIN_ZOOM = 2.0
MAX_ZOOM = 40.0

ZOOM_STEP = 1.1
PAN_SPEED = 10

@dataclass
class Camera:
    screen_width: int
    screen_height: int
    world_width: int
    world_height: int
    
    x: float = 0
    y: float = 0
    zoom: float = DEFAULT_ZOOM

    def world_to_screen(self, position):
        wx, wy = position
        sx = (wx - self.x) * self.zoom
        sy = (wy - self.y) * self.zoom
        return int(sx), int(sy)
    
    def screen_to_world(self, position):
        sx, sy = position
        wx = sx / self.zoom + self.x
        wy = sy / self.zoom + self.y
        return wx, wy
    
    def move(self, dx, dy):
        self.x += dx / self.zoom
        self.y += dy / self.zoom
        self.clamp_to_world()

    def zoom_in(self):
        self.zoom *= ZOOM_STEP
        self.zoom = min(self.zoom, MAX_ZOOM)

    def zoom_out(self):
        self.zoom /= ZOOM_STEP
        self.zoom = max(self.zoom, MIN_ZOOM)

    def clamp_to_world(self):
        max_x = self.world_width - self.screen_width / self.zoom
        max_y = self.world_height - self.screen_height / self.zoom
        self.x = max(0, min(self.x, max_x))
        self.y = max(0, min(self.y, max_y))

    def visible_world_bounds(self):
        left = self.x
        top = self.y
        right = self.x + self.screen_width / self.zoom
        bottom = self.y +self.screen_height / self.zoom
        return left, top, right, bottom
    
    def center_on(self, world_pos):
        wx, wy = world_pos
        self.x = wx - (self.screen_width / self.zoom) / 2
        self.y = wy - (self.screen_height / self.zoom) / 2
        self.clamp_to_world()

    def update(self):
        pass
    