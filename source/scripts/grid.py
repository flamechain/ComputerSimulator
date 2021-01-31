import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 700))

class Pixel:
    def __init__(self, x, y, color, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color

    def isOver(self, pos):
        if self.x*100 < pos[0] < self.x*100+100:
            if self.y*100 < pos[1] < self.y*100+100:
                return True
        return False

    def Draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x*100, self.y*100, 100, 100))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pixels = [
    Pixel(0, 0, WHITE, screen),
    Pixel(1, 0, WHITE, screen),
    Pixel(2, 0, WHITE, screen),
    Pixel(3, 0, WHITE, screen),
    Pixel(4, 0, WHITE, screen),
    Pixel(0, 1, WHITE, screen),
    Pixel(1, 1, WHITE, screen),
    Pixel(2, 1, WHITE, screen),
    Pixel(3, 1, WHITE, screen),
    Pixel(4, 1, WHITE, screen),
    Pixel(0, 2, WHITE, screen),
    Pixel(1, 2, WHITE, screen),
    Pixel(2, 2, WHITE, screen),
    Pixel(3, 2, WHITE, screen),
    Pixel(4, 2, WHITE, screen),
    Pixel(0, 3, WHITE, screen),
    Pixel(1, 3, WHITE, screen),
    Pixel(2, 3, WHITE, screen),
    Pixel(3, 3, WHITE, screen),
    Pixel(4, 3, WHITE, screen),
    Pixel(0, 4, WHITE, screen),
    Pixel(1, 4, WHITE, screen),
    Pixel(2, 4, WHITE, screen),
    Pixel(3, 4, WHITE, screen),
    Pixel(4, 4, WHITE, screen),
    Pixel(0, 5, WHITE, screen),
    Pixel(1, 5, WHITE, screen),
    Pixel(2, 5, WHITE, screen),
    Pixel(3, 5, WHITE, screen),
    Pixel(4, 5, WHITE, screen),
    Pixel(0, 6, WHITE, screen),
    Pixel(1, 6, WHITE, screen),
    Pixel(2, 6, WHITE, screen),
    Pixel(3, 6, WHITE, screen),
    Pixel(4, 6, WHITE, screen)
]

while True:
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in pixels:
                if i.isOver(list(pos)):
                    if i.color == WHITE:
                        i.color = BLACK
                    else:
                        i.color = WHITE
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in pixels:
        i.Draw()

    pygame.display.update()

pygame.quit()
