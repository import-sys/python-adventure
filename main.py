import pygame
from pytmx.util_pygame import load_pygame

def make_game():
    pygame.init()
    pygame.display.set_caption("Python adventure")
    screen = pygame.display.set_mode((800, 640), pygame.RESIZABLE | pygame.SCALED)
    clock = pygame.time.Clock()
    running = True
    game_map = load_pygame("assets/map/map.tmx")
    player_sprite = pygame.image.load("assets/character.png")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_map(game_map, screen)
        game_loop(screen, player_sprite)

        pygame.display.flip()
        clock.tick(60)
       
    pygame.quit()

def draw_map(game_map, screen):
    for layer in game_map.layers:
        for x,y,sprite in layer.tiles():
            screen.blit(sprite, (x * sprite.get_width(), y * sprite.get_height()))


def game_loop(screen, player_sprite):

    # SHOW THE PLAYER
    screen.blit(player_sprite, (720, 450))
    

if __name__ == '__main__':
    make_game()
