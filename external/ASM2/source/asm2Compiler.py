import sys

FILE = sys.argv[1]

with open(FILE, 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()

newlines = []
newline = []

for i in lines:
    j = i[0]
    if j == 'STR':
        newline.append('10000000')
    elif j == 'HLT':
        newline.append('00000000')
    elif j == 'ADD':
        newline.append('00010000')
    elif j == 'IN':
        newline.append('00110000')
    elif j == 'JMP':
        if i[1] != 'IF':
            newline.append('01000000')
        else:
            if i[2] == 'CMP':
                
    elif j == 'GET':
        newline.append('01010000')
    elif j == 'LOAD':
        newline.append('01100000')
    elif j == 'OUT':
        newline.append('01110000')
    elif j == 'SET':
        newline.append('10100000')
    elif j == 'WRT':
        newline.append('10110000')
    elif j == 'SUB':
        newline.append('11000000')
    elif j == 'MULT':
        newline.append('11010000')
    elif j == 'DIV':
        newline.append('11100000')
    elif j == 'BTWS':
        if i[1] == '|':
            newline.append('10010001')
        elif i[1] == '&':
            newline.append('10010000')
        elif i[1] == '~':
            newline.append('10010011')
        elif i[1] == '^':
            newline.append('10010010')
        elif i[1] == '<<':
            newline.append('10010101')
        elif i[1] == '>>':
            newline.append('10010100')
