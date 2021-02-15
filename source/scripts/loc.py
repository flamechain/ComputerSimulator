import sys

path = sys.path[0]

with open(path + '/../bin/' + 'DISK/0000000000000000.bin', 'r') as f:
    data = f.readlines()
