import pygame
from pytmx.util_pygame import load_pygame

from camera import Camera
from gameobjects.npcs.guard import Guard
from gameobjects.npcs.questgiver import QuestGiver
from gameobjects.player import Player
from utils import DrawUtils, InputUtils

map_width = 800
map_height = 640

scale_factor = 3

screen_width = map_width // scale_factor
screen_height = screen_width / 1.78

player = Player(720, 450)
npcs = [
    Guard("Alice", 305, 405),
    Guard("Bob", 160, 375),
    QuestGiver("John", 450, 250),
]

camera = Camera(0, 0, screen_width, screen_height, map_width, map_height)


def game_loop(dt):
    ### ENTER YOUR CODE HERE ###

    player.update(dt)
    player.move(map_width, map_height)
    player.draw(screen, camera)

    for npc in npcs:
        npc.update(dt)
        npc.draw(screen, camera)
        npc.react_to_player(player)

    camera.follow(player)


### DO NOT EDIT BELOW THIS LINE YET ###

pygame.init()
pygame.display.set_caption("Python adventure")
screen = pygame.display.set_mode(
    (screen_width, screen_height), pygame.RESIZABLE | pygame.SCALED
)


def make_game():
    clock = pygame.time.Clock()
    running = True
    game_map = load_pygame("assets/map/map.tmx")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        DrawUtils.draw_map(game_map, screen, camera)
        game_loop(clock.get_time())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    make_game()
