import pygame

from visualization.camera import Camera
from visualization.renderer_agents import AgentRenderer
from visualization.renderer_resources import ResourceRenderer
from visualization.renderer_social import SocialRenderer
from visualization.ui_overlay import UIOverlay

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
BACKGROUND_COLOR = (25, 25, 25)
CAMERA_MOVE_SPEED = 20

class Visualizer:
    def __Init__(self, world):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Epoch")
        self.clock = pygame.time.Clock()

        self.camera = Camera(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            world["width"],
            world["height"]
        )

        self.agent_renderer = AgentRenderer()
        self.resource_renderer = ResourceRenderer()
        self.social_renderer = SocialRenderer()
        self.ui_overlay = UIOverlay()

        self.running = True

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.camera.move(0, -CAMERA_MOVE_SPEED)
        if keys[pygame.K_s]:
            self.camera.move(0, CAMERA_MOVE_SPEED)
        if keys[pygame.K_a]:
            self.camera.move(-CAMERA_MOVE_SPEED, 0)
        if keys[pygame.K_d]:
            self.camera.move(CAMERA_MOVE_SPEED, 0)
        if keys[pygame.K_q]:
            self.camera.zoom_in()
        if keys[pygame.K_e]:
            self.camera.zoom_out()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self, state):
        world = state["world"]
        agents = state["agents"]
        alliances = state["alliances"]
        trades = state["trades"]
        conflicts = state["conflicts"]
        stats = state["stats"]

        self.screen.fill(BACKGROUND_COLOR)
        
        self.resource_renderer.draw(
            self.screen,
            world["resources"],
            self.camera
        )

        self.social_renderer.draw(
            self.screen,
            agents,
            alliances,
            trades,
            conflicts,
            self.camera
        )

        self.agent_renderer.draw(
            self.screen,
            stats
        )

        pygame.display.flip()

    def run(self, state_provider):
        while self.running:
            self.handle_events()
            self.handle_input()
            
            state = state_provider()
            self.render(state)
            self.clock.tick(FPS)

        pygame.quit()