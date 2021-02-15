'''
When you start the computer, it starts with POST checks, which checks
for file corruption and makes sure everything is working fine.
'''

import sys

def post():
    path = sys.path[0]
    if path[-1] == 'S':
        s = '/source'
        s2 = '/source/scripts'
        s3 = ''
    else:
        s = '/..'
        s2 = ''
        s3 = '/../..'

    try:
        with open(path + s + '/bin/DISK/0000000000000000.bin', 'r') as f:
            data = f.readlines()

        with open(path + s + '/bin/RAM.bin', 'r') as f:
            data = f.readlines()

    except:
        return 'Corruption Error: Memory is corrupt'

    try:
        with open(path + s2 + '/ALU.py', 'r') as f:
            data = f.readlines()

        import source.scripts.ALU as ALU

        result = ALU.bitwiseOp('AND', '1', '1')

    except:
        return 'Access Error: Failed to access ALU'

    try:
        import source.scripts.CPU as CPU

        CPU.kernel('00000000000000000000000000000000000000000000000000000000', None, None, None, None)

    except:
        return 'Fatal Error: Kernel failed to operate'

    try:
        with open(path + s3 + '/settings/boot.txt', 'r') as f:
            data = f.readlines()

        if data[0].strip('\n') != "Prefix (UNCHANGABLE) = sys.path[0] + '/../bin/'":
            return 'Corruption Error: boot.bin is corrupt. Fixing data, then re-running.', post()

        with open(path + s3 + '/settings/boot.txt', 'w') as f:
            data[0] = "Prefix (UNCHANGABLE) = sys.path[0] + '/../bin/'\n"
            f.write(''.join(data))

    except:
        return 'Access Error: Failed to load boot settings'
