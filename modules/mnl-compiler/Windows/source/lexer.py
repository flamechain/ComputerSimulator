'''
Converts text into tokens
'''

from .tokens import Token, TokenType
from .exceptions import IllegalChar

WHITESPACE = '\t\n '
DIGITS = '0123456789'
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Lexer:
    '''Converts text into tokens'''
    def __init__(self, text: list) -> None:
        self.text = iter(text)
        self.advance()

    def advance(self) -> None:
        '''Steps through text'''
        try:
            self.currChar = next(self.text) # pylint: disable=C0103

        except StopIteration:
            self.currChar = None

    def generate_tokens(self) -> None:
        '''Creates tokens'''
        while self.currChar is not None:
            if self.currChar in WHITESPACE:
                self.advance()

            elif self.currChar in ['"', "'"]:
                yield self.generate_string()

            elif (self.currChar == '.') | (self.currChar in DIGITS):
                yield self.generate_number()

            elif self.currChar == '+':
                self.advance()
                yield Token(TokenType.PLUS)

            elif self.currChar == '-':
                self.advance()
                yield Token(TokenType.MINUS)

            elif self.currChar == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)

            elif self.currChar == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)

            elif self.currChar == '(':
                self.advance()
                yield Token(TokenType.LPAREN)

            elif self.currChar == ')':
                self.advance()
                yield Token(TokenType.RPAREN)

            else:
                raise IllegalChar(self.currChar)

    def generate_number(self) -> Token:
        '''Creates ints and floats'''
        decimal_count = 0
        number_str = self.currChar
        self.advance()

        while self.currChar is not None:
            if (self.currChar == '.') | (self.currChar in DIGITS):
                if self.currChar == '.':
                    decimal_count += 1

                    if decimal_count > 1:
                        break

                number_str += self.currChar
                self.advance()

            else:
                break

        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str += '0'

        if '.' in number_str:
            result = Token(TokenType.NUMBER, float(number_str))

        else:
            result = Token(TokenType.NUMBER, int(number_str))

        return result

    def generate_string(self) -> Token:
        '''Creates strings'''
        string = self.currChar
        self.advance()
        finall = False

        while self.currChar is not None:
            if self.currChar == string[0]:
                finall = True
            string += self.currChar
            self.advance()
            if finall:
                break

        return Token(TokenType.STRING, str(string))
