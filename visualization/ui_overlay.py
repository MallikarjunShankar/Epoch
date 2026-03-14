import pygame
FONT_SIZE = 16
PANEL_PADDING = 10
LINE_SPACING = 4
TEXT_COLOR = (240, 240, 240)
PANEL_COLOR = (20, 20, 20)
PANEL_ALPHA = 180

class UIOverlay:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("consolas", FONT_SIZE)

    def build_lines(self, stats):
        lines = [
            f"Tick: {stats.get('tick', 0)}",
            f"Agents: {stats.get('agents', 0)}",
            f"Factions: {stats.get('factions', 0)}",
            f"Alliances: {stats.get('alliances', 0)}",
            f"Trades: {stats.get('trades', 0)}",
            f"Conflicts: {stats.get('conflicts', 0)}",
            f"Resources: {stats.get('resources', 0)}",
        ]
        
        return lines
    
    def draw_panel(self, screen, width, height):
        panel_surface = pygame.Surface((width, height))
        panel_surface.set_alpha(PANEL_ALPHA)
        panel_surface.fill(PANEL_COLOR)
        screen.blit(panel_surface, (0, 0))

    def draw(self, screen, stats):
        lines = self.build_lines(stats)
        line_height = self.font.get_height() + LINE_SPACING
        panel_width = 200
        panel_height = len(lines) * line_height + PANEL_PADDING * 2

        self.draw_panel(screen, panel_width, panel_height)
        y = PANEL_PADDING

        for line in lines:
            text_surface = self.font.render(line, True, TEXT_COLOR)
            screen.blit(text_surface, (PANEL_PADDING, y))

            y += line_height