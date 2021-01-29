'''
When you start the computer, it starts with POST checks, then runs BIOS
'''

def POST():
    try:
        with open('DISK/0000000000000000.bin', 'r') as f:
            data = f.readlines()
        with open('RAM.bin', 'r') as f:
            data = f.readlines()
    except:
        return 'Corruption Error: Memory is corrupt'
    try:
        with open('ALU.py', 'r') as f:
            pass
        import ALU
        result = ALU.bitwiseOp('AND', '1', '1')
    except:
        return 'Access Error: Failed to access ALU'
    try:
        from CPU import kernel
        kernel('00000000000000000000000000000000000000000000000000000000')
    except:
        return 'Fatal Error: Kernel failed to operate'

def BIOS(kernel):
    with open('EPROM.bin', 'r') as f: # Gets OS from EPROM
        data = ''.join(f.readlines())
    with open('RAM.bin', 'w') as f: # Wipes RAM and loads OS
        f.write(data)
    kernel('01100000000000000000011000000000010010110000000000000000') # runs start program
