from pixel import Pixel

BLACK = (0, 0, 0)
GREEN = (0, 100, 0)

def mapping(char: str, x: int, y: int, screen) -> list:
    if char == ' ':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == 'A':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'B':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'C':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'D':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'E':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'F':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'G':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'H':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'I':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'J':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'K':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'L':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'M':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'N':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'O':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'P':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'Q':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'R':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'S':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'T':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'U':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'V':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'W':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'X':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'Y':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'Z':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'a':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'b':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'c':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'd':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'e':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'f':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'g':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'h':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'i':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'j':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'k':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'l':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'm':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'n':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'o':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'p':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'q':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'r':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 's':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 't':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'u':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]
    elif char == 'v':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'w':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(GREEN, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'x':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'y':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == 'z':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(GREEN, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == ';':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == ':':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == "'":
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '"':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '/':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '?':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '.':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == ',':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '>':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '<':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '|':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '\\':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == ']':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '}':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '[':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '{':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '=':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '+':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '-':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '_':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == ')':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '(':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(GREEN, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '*':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '&':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(GREEN, x+4, y+6, screen),
        ]

    elif char == '^':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '%':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(GREEN, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '$':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(GREEN, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '#':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(GREEN, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(GREEN, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(GREEN, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(GREEN, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '@':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(GREEN, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(GREEN, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(GREEN, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(GREEN, x+4, y+1, screen),
            Pixel(GREEN, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(GREEN, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(GREEN, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(GREEN, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(GREEN, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(GREEN, x+4, y+4, screen),
            Pixel(GREEN, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(GREEN, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(GREEN, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '!':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(GREEN, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(GREEN, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(GREEN, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(GREEN, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(GREEN, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '`':
        pixels = [
            Pixel(GREEN, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(GREEN, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]

    elif char == '~':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(GREEN, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(GREEN, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(GREEN, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(GREEN, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(GREEN, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '0':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '1':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '2':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '3':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '4':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '5':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '6':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '7':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '8':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    elif char == '9':
        pixels = [
            Pixel(BLACK, x, y, screen),   Pixel(BLACK, x+1, y, screen),   Pixel(BLACK, x+2, y, screen),   Pixel(BLACK, x+3, y, screen),   Pixel(BLACK, x+4, y, screen),
            Pixel(BLACK, x, y+1, screen), Pixel(BLACK, x+1, y+1, screen), Pixel(BLACK, x+2, y+1, screen), Pixel(BLACK, x+3, y+1, screen), Pixel(BLACK, x+4, y+1, screen),
            Pixel(BLACK, x, y+2, screen), Pixel(BLACK, x+1, y+2, screen), Pixel(BLACK, x+2, y+2, screen), Pixel(BLACK, x+3, y+2, screen), Pixel(BLACK, x+4, y+2, screen),
            Pixel(BLACK, x, y+3, screen), Pixel(BLACK, x+1, y+3, screen), Pixel(BLACK, x+2, y+3, screen), Pixel(BLACK, x+3, y+3, screen), Pixel(BLACK, x+4, y+3, screen),
            Pixel(BLACK, x, y+4, screen), Pixel(BLACK, x+1, y+4, screen), Pixel(BLACK, x+2, y+4, screen), Pixel(BLACK, x+3, y+4, screen), Pixel(BLACK, x+4, y+4, screen),
            Pixel(BLACK, x, y+5, screen), Pixel(BLACK, x+1, y+5, screen), Pixel(BLACK, x+2, y+5, screen), Pixel(BLACK, x+3, y+5, screen), Pixel(BLACK, x+4, y+5, screen),
            Pixel(BLACK, x, y+6, screen), Pixel(BLACK, x+1, y+6, screen), Pixel(BLACK, x+2, y+6, screen), Pixel(BLACK, x+3, y+6, screen), Pixel(BLACK, x+4, y+6, screen),
        ]
    else:
        pixels = None
    return pixels
