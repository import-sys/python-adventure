import math

import pygame
from pytmx.util_pygame import load_pygame

screen_width = 800
screen_height = 640

from gameobjects.npc import NPC
from gameobjects.npcs.guard import Guard
from gameobjects.npcs.questgiver import QuestGiver
from gameobjects.player import Player
from utils import DrawUtils, InputUtils

player = Player(720, 450)
npcs = [
    Guard("Alice", 305, 405),
    Guard("Bob", 160, 375),
    QuestGiver("John", 450, 250),
]

NPC.descrease_spot_radius()


def game_loop():

    ### ENTER YOUR CODE HERE ###
    player.reset_velocity()

    if InputUtils.left_pressed():
        player.accelerate_left()
    elif InputUtils.right_pressed():
        player.accelerate_right()

    if InputUtils.up_pressed():
        player.accelerate_up()
    elif InputUtils.down_pressed():
        player.accelerate_down()

    player.move(screen_width, screen_height)

    player.draw(screen)

    for npc in npcs:
        npc.draw(screen)
        npc.react_to_player(player)
        npc.debug_radius_circle(screen)


### DO NOT EDIT BELOW THIS LINE YET ###

pygame.init()
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
        DrawUtils.draw_map(game_map, screen)
        game_loop()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    make_game()
