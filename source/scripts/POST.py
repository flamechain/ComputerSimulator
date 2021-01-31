'''
When you start the computer, it starts with POST checks, which checks
for file corruption and makes sure everything is working fine.
'''

import sys

def post():
    path = sys.path[0]

    try:
        with open(path + '/../bin/DISK/0000000000000000.bin', 'r') as f:
            data = f.readlines()

        with open(path + '/../bin/RAM.bin', 'r') as f:
            data = f.readlines()

    except:
        return 'Corruption Error: Memory is corrupt'

    try:
        with open(path + '/ALU.py', 'r') as f:
            pass

        import ALU

        result = ALU.bitwiseOp('AND', '1', '1')

    except:
        return 'Access Error: Failed to access ALU'

    try:
        import CPU

        CPU.kernel('00000000000000000000000000000000000000000000000000000000', None, None, None, None)

    except:
        return 'Fatal Error: Kernel failed to operate'

    try:
        with open(path + '/../../settings/boot.txt', 'r') as f:
            data = f.readlines()

        if data[0].strip('\n') != "Prefix (UNCHANGABLE) = sys.path[0] + '/../bin/'":
            return 'Corruption Error: boot.bin is corrupt. Fixing data, then re-running.', post()

        with open(path + '/../../settings/boot.txt', 'w') as f:
            data[0] = "Prefix (UNCHANGABLE) = sys.path[0] + '/../bin/'\n"
            f.write(''.join(data))

    except:
        return 'Access Error: Failed to load boot settings'
