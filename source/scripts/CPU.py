'''
File header to create a source function, not for the CPU, only for my code.
'''

import re, sys

def replace(fileName: str, address: int, text: str) -> None:
    '''Function to edit files easier. NOT part of computer, just for my code'''
    path = sys.path[0]
    if path[-1] == 'S':
        s = '/source'
        s2 = '/source/scripts'
        s3 = ''
    else:
        s = '/..'
        s2 = ''
        s3 = '/../..'

    with open(path + s + '/bin/' + fileName, 'r') as f:
        lines = ''.join(f.readlines()).replace('\n', '').replace(' ', '')

    lines = re.findall('........', lines)
    try:
        lines[address] = text
    except:
        print('Address Error: Cant find address {0:b}'.format(address))
        sys.exit()

    with open(path +  s + '/bin/' + fileName, 'w') as f:
        f.write('\n'.join(lines))

'''
Handles basic CPU instructions, and uses ALU
'''

import source.scripts.ALU as ALU

bit = 0 | 1
byte = 8 * bit
path = sys.path[0]
def write(addr: str, data: byte, loc: str = 'RAM.bin') -> None:
    '''Writes to an address'''
    replace(loc, int(addr, 2), str(data))

instruction_set = {
    '0000': 'HLT',
    '0001': 'ADD',
    '0010': 'COMPARE',
    '0011': 'IN',
    '0100': 'JUMP',
    '0101': 'GET',
    '0110': 'LOAD',
    '0111': 'OUT',
    '1000': 'STORE',
    '1001': 'BITWISE',
    '1010': 'SET',
    '1011': 'WRITE',
    '1100': 'SUB',
    '1101': 'MULT',
    '1110': 'DIV',
    '1111': 'JUMP IF'
}

bitwise_set = {
    '0000': 'AND',
    '0001': 'OR',
    '0010': 'XOR',
    '0011': 'NOT',
    '0100': 'RSHFT',
    '0101': 'LSHFT',
    '0110': 'LEF',
    '0111': 'LER',
    '1000': 'BEF',
    '1001': 'BER'
}

registers = {
    '100000000001': 'eax',
    '100000000010': 'ebx',
    '100000000011': 'ecx',
    '100000000100': 'edx'
}

eax = '00000000'
ebx = '00000000'
ecx = '00000000'
edx = '00000000'

def kernel(bootup: str, os: path, ram: path, sector: path, eeprom: path, exc=False) -> None:
    '''Main function to handle hardcoded commands'''
    path = sys.path[0]
    if path[-1] == 'S':
        s = '/source'
        s2 = '/source/scripts'
        s3 = ''
    else:
        s = '/..'
        s2 = ''
        s3 = '/../..'

    statement = [bootup[:4], bootup[8:24], bootup[24:40], bootup[40:56]]
    bootCom = True
    i = int(statement[1], 2)
    end = statement[2]
    instruction = instruction_set[statement[0]]
    while i <= int(end, 2):
        if not bootCom:
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                statement = ''.join(data[i:i+7])
                op = statement[4:8]
                statement = [statement[:4], statement[8:24], statement[24:40], statement[40:56]]
                instruction = instruction_set[statement[0]]

        if instruction == 'HLT':
            if not bootCom:
                command = input().replace(' ', '')
                op = command[4:8]
                statement = [command[:4], command[8:24], command[24:40], command[40:56]]
                instruction = instruction_set[statement[0]]
            else:
                break

        if instruction == 'ADD':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                num1 = data[int(statement[1], 2)]
                num2 = data[int(statement[2], 2)]
            result = ALU.adder8bit(num1, num2)
            write(statement[3], result)

        elif instruction == 'JUMP':
            i = int(statement[1], 2)
            continue

        elif instruction == 'GET':
            with open(path + s + '/bin/DISK/' + statement[1] + '.bin', 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
            currentAddr = statement[2]
            for line in data:
                write(currentAddr, line)
                currentAddr = ALU.increment(currentAddr)

        elif instruction == 'LOAD':
            i = int(statement[1], 2)
            end = statement[2]
            bootCom = False
            continue

        elif instruction == 'STORE':
            if statement[1][0] == '1':
                value = registers[statement[1]]
            else:
                with open(ram, 'r') as f:
                    data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                    data = re.findall('........', data)
                    value = data[int(statement[1], 2)]
            if statement[2][0] == '1':
                value2 = registers[statement[2]]
            else:
                value2 = statement[2]
                write(value2, value)

        elif instruction == 'BITWISE':
            result = ALU.bitwiseOp(bitwise_set[op], statement[1], statement[2])
            write(statement[3], result)

        elif instruction == 'SET':
            write(statement[1], statement[2][:8])

        elif instruction == 'WRITE':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                data = data[int(statement[1], 2):int(statement[2], 2)]
            with open(path + s + '/bin/DISK/' + statement[3] + '.bin', 'w') as f:
                f.write('\n'.join(data))

        elif instruction == 'SUB':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                num1 = data[int(statement[1], 2)]
                num2 = data[int(statement[2], 2)]
            result = ALU.subtract8bit(num1, num2)
            write(statement[3], result)

        elif instruction == 'MULT':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                num1 = data[int(statement[1], 2)]
                num2 = data[int(statement[2], 2)]
            result = ALU.mult8bit(num1, num2)
            write(statement[3], result)

        elif instruction == 'DIV':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                num1 = data[int(statement[1], 2)]
                num2 = data[int(statement[2], 2)]
            result = ALU.div8bit(num1, num2)
            write(statement[3], result)

        elif instruction == 'JUMP IF':
            with open(ram, 'r') as f:
                data = ''.join(f.readlines()).replace(' ', '').replace('\n', '')
                data = re.findall('........', data)
                compare = ''.join(data[int(statement[1], 2):int(statement[1], 2)+7])
                compare = [compare[:4], compare[8:24], compare[24:40], compare[40:56]]
            if instruction_set[compare[0]] == 'COMPARE':
                num1 = data[int(compare[1], 2)]
                num2 = data[int(compare[2], 2)]
                if num1 == num2:
                    i = int(statement[2], 2)
                    end = statement[3]
                    continue

        elif instruction == 'IN':
            pass

        elif instruction == 'OUT':
            pass


        i += 7
        bootCom = False

    if not bootCom:
        if not exc:
            with open(ram, 'w') as f:
                f.write('')
