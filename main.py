import pygame
from pytmx.util_pygame import load_pygame

import math

screen_width = 800
screen_height = 640

player = {
    "x": 720,
    "y": 450,
    "speed_x": 0,
    "speed_y": 0,
    "size": 16
}

npcs = [
        {"name": "Alice", "x": 305, "y": 405, "color": "yellow", "role": "guard", "radius": 40, "size": 16},
        {"name": "Bob", "x": 160, "y": 375, "color": "green", "role": "guard", "radius": 40, "size": 16},
        {"name": "John", "x": 450, "y": 250, "color": "blue", "role": "questgiver", "radius": 20, "size": 16},
]


def get_rectangle_center(x, y, width, height):
    center_x = x + width / 2
    center_y = y + height / 2

    center_point = {
        "x": center_x,
        "y": center_y
    }

    return center_point


def get_distance_between_points(point1, point2):
    dx = point1["x"] - point2["x"]
    dy = point1["y"] - point2["y"]

    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def player_in_npc_radius(player, npc):
    player_center = get_rectangle_center(player["x"], player["y"], player["size"], player["size"])
    npc_center = get_rectangle_center(npc["x"], npc["y"], npc["size"], npc["size"])

    distance = get_distance_between_points(player_center, npc_center)

    return distance <= npc["radius"]


def game_loop():
    ### ENTER YOUR CODE HERE ###
    player["speed_x"] = 0
    player["speed_y"] = 0

    if left_pressed():
        player["speed_x"] = -1
    elif right_pressed():
        player["speed_x"] = 1

    if up_pressed():
        player["speed_y"] = -1
    elif down_pressed():
        player["speed_y"] = 1

    if player["x"] >= 0 and player["x"] + player["size"] <= screen_width:
        player["x"] = player["x"] + player["speed_x"]
    else:
        print("Going offscreen")

    if player["y"] >= 0 and player["y"] + player["size"] <= screen_height:
        player["y"] = player["y"] + player["speed_y"]
    else:
        print("Going offscreen")

    draw_player(player["x"], player["y"])

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
        for x,y,sprite in layer.tiles():
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

if __name__ == '__main__':
    make_game()
