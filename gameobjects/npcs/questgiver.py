import pygame

from animation import Animation
from gameobjects.npc import NPC
from utils import InputUtils, SpritesheetLoader


class QuestGiver(NPC):

    def __init__(self, name, x, y):
        super().__init__(name, x, y, "assets/questgiver.png")
        self.radius = 40

        idle_spritesheet = SpritesheetLoader("assets/questgiver_idle.png", 24, 24)
        self.idle_animation = Animation(idle_spritesheet.get_row(0, 4), 800)

    def react_to_player(self, player):
        if self.player_in_radius(player):
            if InputUtils.is_key_pressed(pygame.K_e):
                print("Hello, adventurer! Your quest is to have fun!")
