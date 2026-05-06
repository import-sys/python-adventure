class Camera:
    def __init__(self, x, y, width, height, map_widht, map_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.map_width = map_widht
        self.map_height = map_height

    def focus(self, x, y):
        self.x = x - self.width // 2
        self.y = y - self.height // 2

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        if self.x + self.width > self.map_width:
            self.x = self.map_width - self.width
        if self.y + self.height > self.map_height:
            self.y = self.map_height - self.height

    def follow(self, gameobject):
        self.focus(gameobject.x, gameobject.y)
