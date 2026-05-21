import pygame


class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.size = 16
        self.sprite = pygame.image.load(image)

    def draw(self, screen, camera):
        screen.blit(self.sprite, (self.x - camera.x, self.y - camera.y))

    def update(self, dt):
        pass
