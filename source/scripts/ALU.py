'''
ALU for CPU
'''

bit = 0 | 1
byte = 8 * bit

def adder(num1: bit, num2: bit, carry: bit) -> [bit, bit]:
    x = num1 ^ num2
    s = x ^ carry
    a = x & carry
    b = num1 & num2
    c = a | b

    return [c, s]

def adder4bit(num1: byte, num2: byte) -> [bit, byte]:
    carry, a = adder(int(num1[3]), int(num2[3]), 0)
    carry, b = adder(int(num1[2]), int(num2[2]), carry)
    carry, c = adder(int(num1[1]), int(num2[1]), carry)
    carry, d = adder(int(num1[0]), int(num2[0]), carry)
    result = str(d) + str(c) + str(b) + str(a)

    return [carry, result]

def adder8bit(num1: byte, num2: byte) -> byte:
    carry, a = adder(int(num1[7]), int(num2[7]), 0)
    carry, b = adder(int(num1[6]), int(num2[6]), carry)
    carry, c = adder(int(num1[5]), int(num2[5]), carry)
    carry, d = adder(int(num1[4]), int(num2[4]), carry)
    carry, e = adder(int(num1[3]), int(num2[3]), carry)
    carry, f = adder(int(num1[2]), int(num2[2]), carry)
    carry, g = adder(int(num1[1]), int(num2[1]), carry)
    carry, h = adder(int(num1[0]), int(num2[0]), carry)
    result = str(h) + str(g) + str(f) + str(e) + str(d) + str(c) + str(b) + str(a)

    return result

def subtracter(num1: bit, num2: bit, borrow: bit) -> [bit, bit]:
    x = num1 ^ num2
    n = 1 - num2
    a = num1 & n
    xn = 1 - x
    a3 = borrow & xn
    a2 = a & a3
    dif = x & borrow

    return [a2, dif]

def subtract8bit(num1: byte, num2: byte) -> byte:
    borrow, a = subtracter(num1[7], num2[7], 0)
    borrow, b = subtracter(num1[6], num2[6], borrow)
    borrow, c = subtracter(num1[5], num2[5], borrow)
    borrow, d = subtracter(num1[4], num2[4], borrow)
    borrow, e = subtracter(num1[3], num2[3], borrow)
    borrow, f = subtracter(num1[2], num2[2], borrow)
    borrow, g = subtracter(num1[1], num2[1], borrow)
    borrow, h = subtracter(num1[0], num2[0], borrow)
    result = str(h) + str(g) + str(f) + str(e) + str(d) + str(c) + str(b) + str(a)

    return result

def increment(num: byte) -> byte:
    return bin(sum([int(num, 2), int('1', 2)]))[2:]

def bitwiseOp(op: str, num1: byte, num2: byte = None) -> byte:
    if op == 'AND':
        result = int(num1, 2) & int(num2, 2)
    elif op == 'OR':
        result = int(num1, 2) | int(num2, 2)
    elif op == 'XOR':
        result = int(num1, 2) ^ int(num2, 2)
    elif op == 'NOT':
        result = ~int(num1, 2)
    elif op == 'LSHFT':
        result = int(num1, 2) << int(num2, 2)
    elif op == 'RSHFT':
        result = int(num1, 2) >> int(num2, 2)

    result = str(result)

    while len(result) < 8:
        result = '0' + result

    return result

def mult4bitUC(num1: byte, num2: byte) -> byte:
    a00 = int(num1[0]) & int(num2[0])
    a01 = int(num1[1]) & int(num2[0])
    a02 = int(num1[2]) & int(num2[0])
    a03 = int(num1[3]) & int(num2[0])
    a10 = int(num1[0]) & int(num2[1])
    a11 = int(num1[1]) & int(num2[1])
    a12 = int(num1[2]) & int(num2[1])
    a13 = int(num1[3]) & int(num2[1])
    a20 = int(num1[0]) & int(num2[2])
    a21 = int(num1[1]) & int(num2[2])
    a22 = int(num1[2]) & int(num2[2])
    a23 = int(num1[3]) & int(num2[2])
    a30 = int(num1[0]) & int(num2[3])
    a31 = int(num1[1]) & int(num2[3])
    a32 = int(num1[2]) & int(num2[3])
    a33 = int(num1[3]) & int(num2[3])
    carry, res1 = adder4bit(str(a13) + str(a12) + str(a11) + str(a10), '0' + str(a03) + str(a02) + str(a01))
    carry, res2 = adder4bit(str(a23) + str(a22) + str(a21) + str(a20), str(carry) + res1[0] + res1[1] + res1[2])
    carry, res3 = adder4bit(str(a33) + str(a32) + str(a31) + str(a30), str(carry) + res2[0] + res2[1] + res2[2])
    result = str(carry) + res3[0] + res3[1] + res3[2] + res3[3] + res2[3] + res1[3] + str(a00)

    return result

def mult8bit(num1: byte, num2: byte) -> byte:
    result = '{0:b}'.format(int(num1, 2)*int(num2, 2))

    while len(result) < 8:
        result = '0' + result

    return result

def div8bit(num1: byte, num2: byte) -> byte:
    result = '{0:b}'.format(int(num1, 2)*int(num1, 2))

    while len(result) < 8:
        result = '0' + result

    return result
