import math

import pygame
from pytmx.util_pygame import load_pygame

screen_width = 800
screen_height = 640


class Player:
    x = 0
    y = 0
    size = 16

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.__speed_x = 0
        self.__speed_y = 0

    def move(self, screen_width, screen_height):
        if self.x >= 0 and self.x + self.size <= screen_width:
            self.x += self.__speed_x

        if self.y >= 0 and self.y + self.size <= screen_height:
            self.y += self.__speed_y

    def reset_velocity(self):
        self.__speed_x = 0
        self.__speed_y = 0

    def accelerate_left(self):
        self.__speed_x = -1

    def accelerate_right(self):
        self.__speed_x = 1

    def accelerate_up(self):
        self.__speed_y = -1

    def accelerate_down(self):
        self.__speed_y = 1


player = Player(720, 450)

npcs = [
    {
        "name": "Alice",
        "x": 305,
        "y": 405,
        "color": "yellow",
        "role": "guard",
        "radius": 40,
        "size": 16,
    },
    {
        "name": "Bob",
        "x": 160,
        "y": 375,
        "color": "green",
        "role": "guard",
        "radius": 40,
        "size": 16,
    },
    {
        "name": "John",
        "x": 450,
        "y": 250,
        "color": "blue",
        "role": "questgiver",
        "radius": 20,
        "size": 16,
    },
]


def get_rectangle_center(x, y, width, height):
    center_x = x + width / 2
    center_y = y + height / 2

    center_point = {"x": center_x, "y": center_y}

    return center_point


def get_distance_between_points(point1, point2):
    dx = point1["x"] - point2["x"]
    dy = point1["y"] - point2["y"]

    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def player_in_npc_radius(player, npc):
    player_center = get_rectangle_center(player.x, player.y, player.size, player.size)
    npc_center = get_rectangle_center(npc["x"], npc["y"], npc["size"], npc["size"])

    distance = get_distance_between_points(player_center, npc_center)

    return distance <= npc["radius"]


def game_loop():
    ### ENTER YOUR CODE HERE ###
    player.reset_velocity()

    if left_pressed():
        player.accelerate_left()
    elif right_pressed():
        player.accelerate_right()

    if up_pressed():
        player.accelerate_up()
    elif down_pressed():
        player.accelerate_down()

    player.move(screen_width, screen_height)

    draw_player(player.x, player.y)

    for npc in npcs:
        draw_rectangle(npc["x"], npc["y"], 16, 16, npc["color"])
        draw_text(npc["name"], npc["x"], npc["y"] - 10, "red")

    for npc in npcs:
        if player_in_npc_radius(player, npc):
            if npc["role"] == "questgiver":
                if is_key_pressed(pygame.K_e):
                    print("Hello, adventurer! Your quest is to have fun!")
            if npc["role"] == "guard":
                npc["color"] = "red"
                print("You shall not pass!")


### DO NOT EDIT BELOW THIS LINE YET ###

pygame.init()
player_sprite = pygame.image.load("assets/character.png")
pygame.display.set_caption("Python adventure")
screen = pygame.display.set_mode((800, 640), pygame.RESIZABLE | pygame.SCALED)


def make_game():
    clock = pygame.time.Clock()
    running = True
    game_map = load_pygame("assets/map/map.tmx")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_map(game_map, screen)
        game_loop()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def draw_map(game_map, screen):
    for layer in game_map.layers:
        for x, y, sprite in layer.tiles():
            screen.blit(sprite, (x * sprite.get_width(), y * sprite.get_height()))


def draw_player(x, y):
    screen.blit(player_sprite, (x, y))


def draw_text(text, x, y, color):
    font = pygame.font.SysFont("Arial", 8)
    drawable = font.render(text, False, color)
    screen.blit(drawable, (x, y))


def draw_rectangle(x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))


def is_key_pressed(key):
    keys = pygame.key.get_pressed()
    return keys[key]


def left_pressed():
    return is_key_pressed(pygame.K_a)


def right_pressed():
    return is_key_pressed(pygame.K_d)


def up_pressed():
    return is_key_pressed(pygame.K_w)


def down_pressed():
    return is_key_pressed(pygame.K_s)


if __name__ == "__main__":
    make_game()
