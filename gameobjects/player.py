from gameobjects.gameobject import GameObject


class Player(GameObject):
    def __init__(self, x, y):

        super().__init__(x, y, "assets/character.png")

        self.__speed_x = 0
        self.__speed_y = 0

    def move(self, screen_width, screen_height):
        if self.x >= 0 and self.x + self.size <= screen_width:
            self.x += self.__speed_x

        if self.y >= 0 and self.y + self.size <= screen_height:
            self.y += self.__speed_y

    def reset_velocity(self):
        self.__speed_x = 0
        self.__speed_y = 0

    def accelerate_left(self):
        self.__speed_x = -1

    def accelerate_right(self):
        self.__speed_x = 1

    def accelerate_up(self):
        self.__speed_y = -1

    def accelerate_down(self):
        self.__speed_y = 1
