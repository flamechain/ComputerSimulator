'''
Operations
'''

from dataclasses import dataclass


@dataclass
class IntegerNode:
    '''Integers'''
    value: int

    def __repr__(self):
        return f'{self.value}'


@dataclass
class StringNode:
    '''Strings'''
    value: str

    def __repr__(self):
        return f'{self.value[1:-1]}'


@dataclass
class ListNode:
    '''Lists'''
    value: list

    def __repr__(self):
        return f'{self.value}'


@dataclass
class ArrayNode:
    '''Arrays'''
    value: list[any]

    def __repr__(self):
        return f'{self.value}'


@dataclass
class DictionaryNode:
    '''Dictionaries'''
    value: dict

    def __repr__(self):
        return f'{self.value}'


@dataclass
class FloatNode:
    '''Floating point numbers'''
    value: float

    def __repr__(self):
        return f'{self.value}'

@dataclass
class AddNode:
    '''Adds'''
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}+{self.node_b})'


@dataclass
class SubtractNode:
    '''Subtracts'''
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}-{self.node_b})'


@dataclass
class MultiplyNode:
    '''Multiplies'''
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}*{self.node_b})'


@dataclass
class DivideNode:
    '''Divides'''
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a}/{self.node_b})'


@dataclass
class PlusNode:
    '''Positive Numbers'''
    node: any

    def __repr__(self):
        return f'(+{self.node})'


@dataclass
class MinusNode:
    '''Negative Numbers'''
    node: any

    def __repr__(self):
        return f'(-{self.node})'
