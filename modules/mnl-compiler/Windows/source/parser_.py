'''
Applies grammar rules
'''

from .tokens import TokenType
from .nodes import FloatNode, IntegerNode, AddNode, SubtractNode, MultiplyNode, DivideNode, PlusNode, MinusNode, StringNode
from .exceptions import SyntaxErrorCust

class Parser:
    '''Parser class'''
    def __init__(self, tokens: list) -> None:
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self) -> None: # pylint: disable=R0201
        '''when called, stops the program and prints an error to the terminal or console'''
        raise SyntaxErrorCust('Invalid syntax')

    def advance(self):
        '''Steps through tokens'''
        try:
            self.current_token = next(self.tokens)

        except StopIteration:
            self.current_token = None

    def parse(self) -> None:
        '''Washes current_token'''
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return result

    def expr(self) -> float:
        '''Priorety branch'''
        result = self.term()

        while self.current_token is not None:
            if self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
                if self.current_token.type == TokenType.PLUS:
                    self.advance()
                    result = AddNode(result, self.term())

                elif self.current_token.type == TokenType.MINUS:
                    self.advance()
                    result = SubtractNode(result, self.term())

            else:
                break

        return result

    def term(self) -> float:
        '''Priorety branch'''
        result = self.factor()

        while self.current_token is not None:
            if self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
                if self.current_token.type == TokenType.MULTIPLY:
                    self.advance()
                    result = MultiplyNode(result, self.factor())

                elif self.current_token.type == TokenType.DIVIDE:
                    self.advance()
                    result = DivideNode(result, self.factor())

            else:
                break

        return result

    def factor(self) -> float: # pylint: disable=R1710
        '''Priorety branch'''
        token = self.current_token
        return_value = None

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance()

            return_value = result

        elif token.type == TokenType.NUMBER:
            self.advance()

            if isinstance(token.type, float):
                return_value = FloatNode(token.value)

            else:
                return_value = IntegerNode(token.value)

        elif token.type == TokenType.STRING:
            self.advance()

            return_value = StringNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()

            return_value = PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()

            return_value = MinusNode(self.factor())

        if return_value is not None:
            return return_value

        self.raise_error()
