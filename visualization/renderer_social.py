import pygame

ALLIANCE_COLOR = (80, 160, 255)
TRADE_COLOR = (255, 220, 80)
CONFLICT_COLOR = (255, 80, 80)
LINE_WIDTH = 1

class SocialRenderer:
    def __init__(self):
        pass
        
    def build_agent_lookup(self, agents):
        return {agent["id"]: agent["position"] for agent in agents}
    
    def draw_links(self, screen, links, agent_lookup, camera, color):
        screen_w, screen_h = screen.get_size()
        for a_id, b_id in links:
            pos_a = agent_lookup.get(a_id)
            pos_b = agent_lookup.get(b_id)

            if not pos_a or not pos_b:
                continue

            sx1, sy1 = camera.world_to_screen(pos_a)
            sx2, sy2 = camera.world_to_screen(pos_b)

            if (
                (sx1 < -20 and sx2 < -20) or
                (sy1 < -20 and sy2 < -20) or
                (sx1 > screen_w + 20 and sx2 > screen_w + 20) or
                (sy1 > screen_h + 20 and sy2 > screen_h + 20)
            ):
                continue

            pygame.draw.line(
                screen,
                color,
                (sx1, sy1),
                (sx2, sy2),
                LINE_WIDTH
            )

    def draw(self, screen, agents, alliances, trades, conflicts, camera):
        agent_lookup = self.build_agent_lookup(agents)
        self.draw_links(
            screen,
            alliances,
            agent_lookup,
            camera,
            ALLIANCE_COLOR
        )

        self.draw_links(
            screen,
            trades,
            agent_lookup,
            camera,
            TRADE_COLOR
        )

        self.draw_links(
            screen,
            conflicts,
            agent_lookup,
            camera,
            CONFLICT_COLOR
        )