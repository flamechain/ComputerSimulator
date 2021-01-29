'''
Value Types
'''

from dataclasses import dataclass
from typing import Any


@dataclass
class Integer:
    '''Integers'''
    value: int

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Float:
    '''Floating point numbers'''
    value: float

    def __repr__(self):
        return f'{self.value}'


@dataclass
class String:
    '''A string of characters'''
    value: str

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Array:
    '''A collection of items'''
    value: list[type]

    def __repr__(self):
        return f'{self.value}'


@dataclass
class List:
    '''A collection of any items'''
    value: list

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Dictionary:
    '''A collection of keys'''
    value: dict

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Null:
    '''None'''
    value: None

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Boolean:
    '''Boolean'''
    value: bool

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Bytes:
    '''Byte'''
    value: bytes

    def __repr__(self):
        return f'{self.value}'
