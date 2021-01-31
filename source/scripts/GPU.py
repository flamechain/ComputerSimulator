import pygame, threading, time
from char_map1 import mapping

pygame.init()

screen = pygame.display.set_mode((1920, 1060), pygame.RESIZABLE)

class Char:
    def __init__(self, x: int, y: int, char: str, screen: object):
        x *= 6
        y *= 8
        self.pixels = mapping(char, x, y, screen)

    def Draw(self) -> None:
        if self.pixels is not None:
            for i in self.pixels:
                i.Draw()
