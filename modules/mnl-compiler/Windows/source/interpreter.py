'''
Applies operations
'''

from typing import Any
from .values import Float, Integer, String
from .exceptions import DivisionByZero


class Interpreter:
    '''Applies operations'''
    def visit(self, node: object) -> Any:
        '''Fetches current node'''
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)

        return method(node)

    def visit_IntegerNode(self, node: object) -> Integer: # pylint: disable=R0201, C0103
        '''Visits IntegerNode'''
        return Integer(node.value)

    def visit_FloatNode(self, node: object) -> Float:
        '''Visits FloatNode'''
        return Float(node.value)

    def visit_StringNode(self, node: object) -> String:
        '''Visits StringNode'''
        return String(node.value)

    def visit_AddNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits AddNode'''
        if isinstance(node.node_a.value, int) & isinstance(node.node_b.value, int):
            result = Integer(self.visit(node.node_a).value + self.visit(node.node_b).value).value

        elif isinstance(node.node_a.value, str) & isinstance(node.node_b.value, str):
            result = String(self.visit(node.node_a).value[1:-1] + self.visit(node.node_b).value[1:-1]).value

        else:
            result = Float(self.visit(node.node_a).value + self.visit(node.node_b).value).value

        return result

    def visit_SubtractNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits SubtractNode'''
        if isinstance(node.node_a.value, int) & isinstance(node.node_b.value, int):
            result = Integer(self.visit(node.node_a).value - self.visit(node.node_b).value).value

        else:
            result = Float(self.visit(node.node_a).value - self.visit(node.node_b).value).value

        return result

    def visit_MultiplyNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits MultiplyNode'''
        if isinstance(node.node_a.value, int) & isinstance(node.node_b.value, int):
            result = Integer(self.visit(node.node_a).value * self.visit(node.node_b).value).value

        else:
            result = Float(self.visit(node.node_a).value * self.visit(node.node_b).value).value

        return result

    def visit_DivideNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits DivideNode'''
        try:
            if isinstance(node.node_a.value, int) & isinstance(node.node_b.value, int):
                result = Integer(self.visit(node.node_a).value / self.visit(node.node_b).value).value

            else:
                result = Float(self.visit(node.node_a).value / self.visit(node.node_b).value).value

            return result

        except:
            raise DivisionByZero() # pylint: disable=W0707

    def visit_PlusNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits PlusNode'''
        if isinstance(node.node.value, int):
            result = Integer(self.visit(node.node).value).value

        else:
            result = Float(self.visit(node.node).value).value

        return result

    def visit_MinusNode(self, node: object) -> Any: # pylint: disable=C0103
        '''Visits MinusNode'''
        if isinstance(node.node.value, int):
            result = Integer(-self.visit(node.node).value).value

        else:
            result = Float(-self.visit(node.node).value).value

        return result
