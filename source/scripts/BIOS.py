'''
BIOS gets location of everything, and sends those locations to the kernel,
and then loads the eprom (os) into ram and runs the os. The os will copy
the program from the boot sector, and run that.
'''

from source.scripts.graphics_card import GPU
from source.scripts.char_to_bin import symbol_table
import sys, threading, time

def bios(kernel, screen):
    path = sys.path[0]
    if path[-1] == 'S':
        s = '/source'
        s2 = '/source/scripts'
        s3 = ''
    else:
        s = '/..'
        s2 = ''
        s3 = '/../..'

    with open(path + s3 + '/settings/boot.txt') as f:
        data = f.readlines()

        for i in data:
            if 'Boot Sector' in i:
                boot_sector = path + s + '/bin/' + i.replace('Boot Sector:', '').replace(' ', '').strip('\n')

            elif 'OS Location' in i:
                os = path + s + '/bin/' + i.replace('OS Location:', '').replace(' ', '').strip('\n')

            elif 'RAM Location' in i:
                ram = path + s + '/bin/' + i.replace('RAM Location:', '').replace(' ', '').strip('\n')

            elif 'Additional' in i:
                eeprom = path + s + '/bin/' + i.replace('Additional:', '').replace(' ', '').strip('\n')

            elif 'GPU Address' in i:
                gpu_addr = path + s + '/bin/' + i.replace('GPU Address:', '').replace(' ', '').strip('\n')

    with open(os, 'r') as f:
        data = ''.join(f.readlines())

    with open(ram, 'w') as f:
        f.write(data)

    gpu = GPU(screen, gpu_addr)

    def refresh(rate):
        while True:
            gpu.update()
            time.sleep((1 / rate))

    t = threading.Thread(target=refresh, args=[30])
    t.start()

    boot_text = 'POST Results:\n    All checks successfull\nRAM: 64 kg, 63 kg free\nDISK: 4 mg, 4 mg free\nGraphics Card: 0000000000000001'
    boot_data = ''
    x = 2
    y = 2
    for i in boot_text:
        if i == '\n':
            y += 1
            x = 2
            continue
        for j in symbol_table:
            if symbol_table[j] == i:
                boot_data += j + '\n'
                new_x = '{0:b}'.format(x)
                while len(new_x) < 8:
                    new_x = '0' + new_x
                new_y = '{0:b}'.format(y)
                while len(new_y) < 8:
                    new_y = '0' + new_y
                boot_data += new_x + '\n' + new_y + '\n'
                break
        x += 1

    with open(gpu_addr, 'w') as f:
        f.write(boot_data)
    kernel('01100000000000000000000000000000000001100000000000000000', os, ram, boot_sector, eeprom, exc=True)
    kernel('01100000000000000000011000000000010010110000000000000000', os, ram, boot_sector, eeprom)
    time.sleep(1)
    with open(gpu_addr, 'w') as f:
        f.write('')
