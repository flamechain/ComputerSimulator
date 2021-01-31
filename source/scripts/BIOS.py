'''
BIOS gets location of everything, and sends those locations to the kernel,
and then loads the eprom (os) into ram and runs the os. The os will copy
the program from the boot sector, and run that.
'''

import sys

def bios(kernel):
    path = sys.path[0]

    with open(path + '/../../settings/boot.txt') as f:
        data = f.readlines()

        for i in data:
            if 'Boot Sector' in i:
                boot_sector = path + '/../bin/' + i.replace('Boot Sector:', '').replace(' ', '').strip('\n')

            elif 'OS Location' in i:
                os = path + '/../bin/' + i.replace('OS Location:', '').replace(' ', '').strip('\n')

            elif 'RAM Location' in i:
                ram = path + '/../bin/' + i.replace('RAM Location:', '').replace(' ', '').strip('\n')

            elif 'Additional' in i:
                eeprom = path + '/../bin/' + i.replace('Additional:', '').replace(' ', '').strip('\n')

    with open(os, 'r') as f:
        data = ''.join(f.readlines())

    with open(ram, 'w') as f:
        f.write(data)

    kernel('01100000000000000000000000000000000001100000000000000000', os, ram, boot_sector, eeprom, exc=True)
    kernel('01100000000000000000011000000000010010110000000000000000', os, ram, boot_sector, eeprom)
