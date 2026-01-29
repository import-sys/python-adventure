import pygame
from pytmx.util_pygame import load_pygame

player_x = 720
player_y = 450


screen_width = 800
screen_height = 640

player_width = 16
player_height = 16


def game_loop():
    ### ENTER YOUR CODE HERE ###

    global player_x, player_y

    player_speed_x = 1
    player_speed_y = 1


    if player_x >= 0 and player_x + player_width <= screen_width:
        player_x = player_x + player_speed_x

    if player_y >= 0 and player_y + player_height <= screen_height:
        player_y = player_y + player_speed_y

    draw_player(player_x, player_y)


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
