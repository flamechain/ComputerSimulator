import pygame
from source.scripts.char_map1 import mapping

class Char:
    def __init__(self, x: int, y: int, char: str, screen: object):
        x *= 6
        y *= 8
        self.pixels = mapping(char, x, y, screen)

    def Draw(self) -> None:
        if self.pixels is not None:
            for i in self.pixels:
                i.Draw()
