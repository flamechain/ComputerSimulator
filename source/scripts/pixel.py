import pygame

class Pixel:
    def __init__(self, color: tuple, x: int, y: int, screen: object, size: int = 3):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.size = size

    def Draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size))
