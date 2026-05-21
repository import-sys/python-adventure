from animation import Animation
from gameobjects.npc import NPC
from utils import SpritesheetLoader


class Guard(NPC):
    def __init__(self, name, x, y):
        super().__init__(name, x, y, "assets/guard.png")

        idle_spritesheet = SpritesheetLoader("assets/guard_idle.png", 24, 24)
        self.idle_animation = Animation(idle_spritesheet.get_row(0, 4), 800)

    def react_to_player(self, player):
        if self.player_in_radius(player):
            self.color = "red"
            print("You shall not pass!")
