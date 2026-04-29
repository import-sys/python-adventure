import pygame

from gameobjects.npc import NPC
from utils import InputUtils


class QuestGiver(NPC):

    def __init__(self, name, x, y):
        super().__init__(name, x, y, "assets/questgiver.png")
        self.radius = 40

    def react_to_player(self, player):
        if self.player_in_radius(player):
            if InputUtils.is_key_pressed(pygame.K_e):
                print("Hello, adventurer! Your quest is to have fun!")
