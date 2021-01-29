'''
Error handling classes
'''

class Error(Exception):
    '''Base error class'''


class RuntimeErrorCust(Error):
    '''Runtime base class'''


class IllegalChar(Error):
    '''Illegal Character error'''
    __module__ = Exception.__module__


class DivisionByZero(RuntimeErrorCust):
    '''Division by zero error'''
    __module__ = 'RuntimeError'


class SyntaxErrorCust(RuntimeErrorCust):
    '''Syntax error'''
    __module__ = 'RuntimeError'


class ExceptError(Error):
    '''Error to manually break from try'''
    __module__ = Exception.__module__
