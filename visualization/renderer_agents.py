import pygame

BASE_AGENT_RADIUS = 3
DEFAULT_AGENT_COLOR = (200, 200, 200)

STATE_COLORS = {
    "neutral": None,
    "trading": (255, 220, 0),
    "fighting": (255, 60, 60),
}

FACTION_COLORS = {
    None: (200, 200, 200),
}

class AgentRenderer:
    def __init__(self, faction_colors = None):
        if faction_colors:
            FACTION_COLORS.update(faction_colors)

    def get_agent_color(self, agent):
        faction = agent.get("faction")
        return FACTION_COLORS.get(faction, DEFAULT_AGENT_COLOR)
    
    def compute_radius(self, agent, camera):
        energy = agent.get("energy", 0)
        base = BASE_AGENT_RADIUS * camera.zoom * 0.25
        radius = base + (energy * 0.02)
        return max(2, int(radius))
    
    def draw_agent(self, screen, agent, camera):
        sx, sy = camera.world_to_screen(agent["position"])
        screen_w, screen_h = screen.get_size()

        if sx < -10 or sy < -10 or sx > screen_w + 10 or sy > screen_h + 10:
            return
        
        color = self.get_agent_color(agent)
        radius = self.compute_radius(agent, camera)
        pygame.draw.circle(screen, color, (sx, sy), radius)

        state = agent.get("state")
        state_color = STATE_COLORS.get(state)

        if state_color:
            pygame.draw.circle(
                screen,
                state_color,
                (sx, sy),
                radius + 2,
                1
            )
    
    def draw(self, screen, agents, camera):
        for agent in agents:
            self.draw_agent(screen, agent, camera)
