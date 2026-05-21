import pygame

from animation import Animation
from gameobjects.gameobject import GameObject
from utils import InputUtils, SpritesheetLoader


class Player(GameObject):
    def __init__(self, x, y):

        super().__init__(x, y, "assets/character.png")

        self.direction = "F"

        idle_spritesheet = SpritesheetLoader("assets/player_idle.png", 24, 24)
        running_spritesheet = SpritesheetLoader("assets/player_running.png", 24, 24)

        self.idle_animation = {
            "F": Animation(idle_spritesheet.get_row(0, 4), 800),
            "L": Animation(idle_spritesheet.get_row(1, 4), 800),
            "R": Animation(idle_spritesheet.get_row(2, 4), 800),
            "B": Animation(idle_spritesheet.get_row(3, 4), 800),
        }
        self.running_animation = {
            "F": Animation(running_spritesheet.get_row(0, 4), 800),
            "L": Animation(running_spritesheet.get_row(1, 4), 800),
            "R": Animation(running_spritesheet.get_row(2, 4), 800),
            "B": Animation(running_spritesheet.get_row(3, 4), 800),
        }

        self.__speed_x = 0
        self.__speed_y = 0

    def update(self, dt):
        self.reset_velocity()

        if InputUtils.left_pressed():
            self.accelerate_left()
        elif InputUtils.right_pressed():
            self.accelerate_right()

        if InputUtils.up_pressed():
            self.accelerate_up()
        elif InputUtils.down_pressed():
            self.accelerate_down()
    
        if self.is_moving():
            self.idle_animation[self.direction].stop()
            self.sprite = self.running_animation[self.direction].play(dt)
        else:
            self.running_animation[self.direction].stop()
            self.sprite = self.idle_animation[self.direction].play(dt)

    def move(self, screen_width, screen_height):
        if self.x >= 0 and self.x + self.size <= screen_width:
            self.x += self.__speed_x

        if self.y >= 0 and self.y + self.size <= screen_height:
            self.y += self.__speed_y

    def reset_velocity(self):
        self.__speed_x = 0
        self.__speed_y = 0

    def is_moving(self):
        return self.__speed_x != 0 or self.__speed_y != 0

    def accelerate_left(self):
        self.__speed_x = -1
        self.direction = "L"

    def accelerate_right(self):
        self.__speed_x = 1
        self.direction = "R"

    def accelerate_up(self):
        self.__speed_y = -1
        self.direction = "B"

    def accelerate_down(self):
        self.__speed_y = 1
        self.direction = "F"
