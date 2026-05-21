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
    def draw_map(game_map, screen, camera):
        for layer in game_map.layers:
            for x, y, sprite in layer.tiles():
                screen.blit(
                    sprite,
                    (
                        x * sprite.get_width() - camera.x,
                        y * sprite.get_height() - camera.y,
                    ),
                )

    @staticmethod
    def draw_text(screen, text, x, y, color):
        font = pygame.font.SysFont("JetBrainsMonoNerdFont", 8)
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


class SpritesheetLoader:
    def __init__(self, spritesheet, frame_width, frame_height):
        self.spritesheet = pygame.image.load(spritesheet)
        self.frame_width = frame_width
        self.frame_height = frame_height

    def get_frame(self, row_id, frame_id):
        x_offset = frame_id * self.frame_width
        y_offset = row_id * self.frame_height

        return self.spritesheet.subsurface(
            (x_offset, y_offset, self.frame_width, self.frame_height)
        )

    def get_row(self, row_id, frames_count):
        frames = []
        for frame_id in range(0, frames_count):
            frames.append(self.get_frame(row_id, frame_id))

        return frames
