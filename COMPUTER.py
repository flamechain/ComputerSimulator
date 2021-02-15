from source.scripts.POST import post
from source.scripts.BIOS import bios
from source.scripts.CPU import kernel
import pygame, threading, sys, time

def boot(screen):
    Error = post()
    if Error is not None:
        print(Error)
        sys.exit()
    else:
        bios(kernel, screen)

pygame.init()
screen = pygame.display.set_mode((1920, 1050), pygame.RESIZABLE)
t = threading.Thread(target=boot, args=[screen])
t.start()
print('_'*71 + '\n')
run = True
screen.fill((0, 0, 0))
caps = False
x = 2
y = 2
code = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            code = None
            if event.key == pygame.K_a:
                code = '00000000' if caps else '00011010'
            elif event.key == pygame.K_b:
                code = '00000001' if caps else '00011011'
            elif event.key == pygame.K_c:
                code = '00000010' if caps else '00011100'
            elif event.key == pygame.K_d:
                code = '00000011' if caps else '00011101'
            elif event.key == pygame.K_e:
                code = '00000100' if caps else '00011110'
            elif event.key == pygame.K_f:
                code = '00000101' if caps else '00011111'
            elif event.key == pygame.K_g:
                code = '00000110' if caps else '00100000'
            elif event.key == pygame.K_h:
                code = '00000111' if caps else '00100001'
            elif event.key == pygame.K_i:
                code = '00001000' if caps else '00100010'
            elif event.key == pygame.K_j:
                code = '00001001' if caps else '01011100'
            elif event.key == pygame.K_k:
                code = '00001010' if caps else '00100011'
            elif event.key == pygame.K_l:
                code = '00001011' if caps else '00100100'
            elif event.key == pygame.K_m:
                code = '00001100' if caps else '00100101'
            elif event.key == pygame.K_n:
                code = '00001101' if caps else '00100110'
            elif event.key == pygame.K_o:
                code = '00001110' if caps else '00100111'
            elif event.key == pygame.K_p:
                code = '00001111' if caps else '00101000'
            elif event.key == pygame.K_q:
                code = '00010000' if caps else '00101001'
            elif event.key == pygame.K_r:
                code = '00010001' if caps else '00101010'
            elif event.key == pygame.K_s:
                code = '00010010' if caps else '00101011'
            elif event.key == pygame.K_t:
                code = '00010011' if caps else '00101100'
            elif event.key == pygame.K_u:
                code = '00010100' if caps else '01011101'
            elif event.key == pygame.K_v:
                code = '00010101' if caps else '00101101'
            elif event.key == pygame.K_w:
                code = '00010110' if caps else '00101110'
            elif event.key == pygame.K_x:
                code = '00010111' if caps else '00101111'
            elif event.key == pygame.K_y:
                code = '00011000' if caps else '00110000'
            elif event.key == pygame.K_z:
                code = '00011001' if caps else '00110001'
            elif event.key == pygame.K_LSHIFT:
                caps = True
            elif event.key == pygame.K_TAB:
                code = '01011100'
            elif event.key == pygame.K_SPACE:
                code = '01011100'
            elif event.key == pygame.K_BACKSPACE:
                code = '01011101'
            elif event.key == pygame.K_EXCLAIM:
                code = '01011001'
            elif event.key == pygame.K_SEMICOLON:
                code = '00111100'
            elif event.key == pygame.K_COLON:
                code = '00111101'
            elif event.key == pygame.K_QUOTE:
                code = '00111110'
            elif event.key == pygame.K_QUOTEDBL:
                code = '00111111'
            elif event.key == pygame.K_SLASH:
                code = '01000000' if not caps else '01000111'
            elif event.key == pygame.K_BACKSLASH:
                code = '01000001'
            elif event.key == pygame.K_QUESTION:
                code = '01000010'
            elif event.key == pygame.K_PERIOD:
                code = '01000011'
            elif event.key == pygame.K_COMMA:
                code = '01000100'
            elif event.key == pygame.K_LESS:
                code = '01000101'
            elif event.key == pygame.K_GREATER:
                code = '01000110'
            elif event.key == pygame.K_RIGHTBRACKET:
                code = '01001000' if not caps else '01001101'
            elif event.key == pygame.K_LEFTBRACKET:
                code = '01001001' if not caps else '01001100'
            elif event.key == pygame.K_LEFTPAREM:
                code = '01001010'
            elif event.key == pygame.K_RIGHTPAREN:
                code = '01001011'
            elif event.key == pygame.K_EQUALS:
                code = '01001110'
            elif event.key == pygame.K_KP_PLUS:
                code = '01001111'
            elif event.key == pygame.K_KP_MINUS:
                code = '01010000'
            elif event.key == pygame.K_UNDERSCORE:
                code = '01010001'
            elif event.key == pygame.K_KP_MULTIPLY:
                code = '01010010'
            elif event.key == pygame.K_CARET:
                code = '01010011'
            elif event.key == pygame.K_AMPERSAND:
                code = '01010100'
            elif event.key == pygame.K_DOLLAR:
                code = '01010110'
            elif event.key == pygame.K_HASH:
                code = '01010111'
            elif event.key == pygame.K_AT:
                code = '01011000'
            elif event.key == pygame.K_EXCLAIM:
                code = '01011001'
            elif event.key == pygame.K_BACKQUOTE:
                code = '01011011' if not caps else '01011010'
            elif event.key == pygame.K_0:
                code = '00110010'
            elif event.key == pygame.K_1:
                code = '00110011'
            elif event.key == pygame.K_2:
                code = '00110100'
            elif event.key == pygame.K_3:
                code = '00110101'
            elif event.key == pygame.K_4:
                code = '00110110'
            elif event.key == pygame.K_5:
                code = '00110111' if not caps else '01010101'
            elif event.key == pygame.K_6:
                code = '00111000'
            elif event.key == pygame.K_7:
                code = '00111001'
            elif event.key == pygame.K_8:
                code = '00111010'
            elif event.key == pygame.K_9:
                code = '00111011'
            elif event.key == pygame.ENTER:
                code = '01011110'
            
            if code is not None:
                with open(sys.path[0] + '/source/bin/DISK/0000000000000010.bin', 'w') as f: f.write(code)
                if code == '01011110':
                    y += 1
                elif code == '01011101':
                    x -= 1
                    with open(sys.path[0] + '/source/bin/DISK/0000000000000001.bin', 'r') as f:
                        data = f.readlines()[:-3]
                    with open(sys.path[0] + '/source/bin/DISK/0000000000000001.bin', 'w') as f:
                        f.write(''.join(data))
                else:
                    new_y = '{0:b}'.format(y)
                    new_x = '{0:b}'.format(x)
                    while len(new_x) < 8: new_x = '0' + new_x
                    while len(new_y) < 8: new_y = '0' + new_y
                    with open(sys.path[0] + '/source/bin/DISK/0000000000000001.bin', 'a') as f:
                        f.write(code + f'\n{new_x}\n{new_y}')
                    x += 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                caps = False

    pygame.display.update()

pygame.quit()
sys.exit()
