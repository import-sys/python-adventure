import math

import pygame


class GeometryUtils:
    @staticmethod
    def get_rectangle_center(x, y, width, height):
        center_x = x + width / 2
        center_y = y + height / 2

        center_point = {"x": center_x, "y": center_y}

        return center_point

    @staticmethod
    def get_distance_between_points(point1, point2):
        dx = point1["x"] - point2["x"]
        dy = point1["y"] - point2["y"]

        distance = math.sqrt(dx * dx + dy * dy)

        return distance


class DrawUtils:
    @staticmethod
    def draw_map(game_map, screen):
        for layer in game_map.layers:
            for x, y, sprite in layer.tiles():
                screen.blit(sprite, (x * sprite.get_width(), y * sprite.get_height()))

    @staticmethod
    def draw_text(screen, text, x, y, color):
        font = pygame.font.SysFont("Arial", 8)
        drawable = font.render(text, False, color)
        screen.blit(drawable, (x, y))

    @staticmethod
    def draw_rectangle(screen, x, y, w, h, color):
        pygame.draw.rect(screen, color, (x, y, w, h))


class InputUtils:
    @staticmethod
    def is_key_pressed(key):
        keys = pygame.key.get_pressed()
        return keys[key]

    @staticmethod
    def left_pressed():
        return InputUtils.is_key_pressed(pygame.K_a)

    @staticmethod
    def right_pressed():
        return InputUtils.is_key_pressed(pygame.K_d)

    @staticmethod
    def up_pressed():
        return InputUtils.is_key_pressed(pygame.K_w)

    @staticmethod
    def down_pressed():
        return InputUtils.is_key_pressed(pygame.K_s)
