from POST import post
from BIOS import bios
from CPU import kernel
from GPU import Char
import pygame, threading, sys, time

def boot():
    time.sleep(1)
    Error = post()
    if Error is not None:
        print(Error)
        sys.exit()
    else:
        bios(kernel)

t = threading.Thread(target=boot)
t.start()
pygame.init()
screen = pygame.display.set_mode((1920, 1050), pygame.RESIZABLE)
print('\033[F'*3)
run = True
screen.fill((0, 0, 0))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
