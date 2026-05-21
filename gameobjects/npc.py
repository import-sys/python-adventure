import pygame

from gameobjects.gameobject import GameObject
from utils import DrawUtils, GeometryUtils


class NPC(GameObject):
    color = "green"
    radius = 40

    @classmethod
    def descrease_spot_radius(cls):
        cls.radius = cls.radius // 2

    def __init__(self, name, x, y, image):

        super().__init__(x, y, image)
        self.idle_animation = None
        self.name = name

    def update(self, dt):
        if self.idle_animation is not None:
            self.sprite = self.idle_animation.play(dt)

    def draw(self, screen, camera):
        super().draw(screen, camera)

        DrawUtils.draw_text(
            screen, self.name, self.x - camera.x, self.y - 10 - camera.y, self.color
        )

    def player_in_radius(self, player):
        player_center = GeometryUtils.get_rectangle_center(
            player.x, player.y, player.size, player.size
        )
        npc_center = GeometryUtils.get_rectangle_center(
            self.x, self.y, self.size, self.size
        )

        distance = GeometryUtils.get_distance_between_points(player_center, npc_center)

        return distance <= self.radius

    def react_to_player(self, player):
        pass

    def debug_radius_circle(self, screen):
        npc_center = GeometryUtils.get_rectangle_center(
            self.x, self.y, self.size, self.size
        )

        pygame.draw.circle(
            screen, self.color, (npc_center["x"], npc_center["y"]), self.radius, 1
        )
