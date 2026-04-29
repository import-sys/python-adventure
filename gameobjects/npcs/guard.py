from gameobjects.npc import NPC


class Guard(NPC):
    def __init__(self, name, x, y):
        super().__init__(name, x, y, "assets/guard.png")

    def react_to_player(self, player):
        if self.player_in_radius(player):
            self.color = "red"
            print("You shall not pass!")
