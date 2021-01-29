'''
Used to help after the splitting into tokens, to help transfer quick number data
'''

from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    '''class to give tokens an id'''
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6
    STRING = 7


@dataclass
class Token:
    '''Token Object'''
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f'{self.value}' if self.value is not None else '')
