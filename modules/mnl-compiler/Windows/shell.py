'''
Interactive Shell
'''

from source.lexer import Lexer
from source.parser_ import Parser
from source.interpreter import Interpreter
from source.exceptions import IllegalChar, DivisionByZero, SyntaxErrorCust, ExceptError

with open("Help/release_info.md", "r") as file_:
    info = []
    lines = file_.readlines()

    for line in lines:
        if line == '\n':
            continue

        if line[0] == '#':
            continue

        if line.strip('\n') == '\\':
            info.append('')
            continue

        info.append(line.strip('\n'))

def preinfo(info_list: list) -> None:
    '''Handles non-loop info'''
    name = info_list[0]
    version = info_list[1]
    tags = info_list[2]
    osinfo = info_list[3]
    system = info_list[4]
    print('%s %s (%s) [%s] on %s' % (name, version, tags, osinfo, system))
    print('Type "help", "copyright", "credits", or "license" for more information.')


class Helper:                                                                                                       # pylint: disable=R0903, R0902
    '''Simlar to Python help() function'''
    def __init__(self, keyword: object = None) -> None:
        self.info = []

        with open('Help/source/help_source.txt', 'r') as file_:                                                               # pylint: disable=W0621
            lines = file_.readlines()                                                                               # pylint: disable=W0621

            for line in lines:                                                                                      # pylint: disable=W0621
                if line == '\n':
                    continue

                if line[0] == '#':
                    continue

                if line.strip('\n') == '\\':
                    self.info.append('')
                    continue

                self.info.append(line.strip('\n\\n'))

        self.object = keyword

        self.keywords =    '\n'.join(self.info[self.info.index('// Keywords')+1:self.info.index('// Symbols')])     # pylint: disable=C0301
        self.symbols =     '\n'.join(self.info[self.info.index('// Symbols')+1:self.info.index('// Symbol Table')]) # pylint: disable=C0301
        self.topics =      '\n'.join(self.info[self.info.index('// Topics')+1:self.info.index('<Topics End>')])     # pylint: disable=C0301
        self.modules =     '\n'.join(self.info[self.info.index('// Modules')+1:self.info.index('// Keywords')])     # pylint: disable=C0301
        self.description = '\n'.join(self.info[self.info.index('// Help')+1:self.info.index('// Modules')])         # pylint: disable=C0301
        self.symbol_table = '\n'.join(self.info[self.info.index('// Symbol Table')+1:self.info.index('// Topics')]) # pylint: disable=C0301
        self.literals = self.symbols.replace('\n', '').replace(' ', '')

        if self.object is None:
            print(self.description)

    def help_loop(self) -> bool:                                                                                    # pylint: disable=R0912
        '''Loop that contains helper'''
        help_run = True

        while help_run:
            if self.object is not None:
                help_com = self.object

            else:
                help_com = input('help> ').lower()

            if help_com == 'modules':
                print(self.modules)

            elif help_com == 'keywords':
                print(self.keywords)

            elif help_com == 'symbols':
                print(self.symbols)

            elif help_com == 'topics':
                print(self.topics)

            elif help_com in ['q', 'quit']:
                help_run = False
                print('You are leaving help and returning to the MNL interpreter.')
                return 'soft'

            elif help_com == 'quit()':
                help_run = False
                return 'hard'

            elif help_com in self.literals:
                print(self.symbol_table)

            elif help_com.upper() in self.topics.split('\n'):
                topic = '// ' + help_com[0].upper()
                topic += help_com[1:].lower()
                last = 0

                try:
                    temp = self.topics.split('\n')[self.topics.split('\n').index(help_com.upper())+1]               # pylint: disable=C0301

                    if temp in [None, '\n', '']:
                        raise ExceptError()

                    temp2 = '// ' + temp[0].upper()
                    temp2 += temp[1:].lower()

                except ExceptError:
                    temp2 = self.info[-1]
                    last = 1

                search = '\n'.join(self.info[self.info.index(topic)+1:self.info.index(temp2)+last])
                print(search)


CREDITS = '\n'.join(info[info.index('// Credits')+1:info.index('// Copyright')])
COPYRIGHT = '\n'.join(info[info.index('// Copyright')+1:info.index('// License')])
LICENSE = '\n'.join(info[info.index('// License')+1:len(info)])

preinfo(info)

run = True                                                                                                          # pylint: disable=C0103

while run:
    command = input('>>> ').lower()

    if command == 'help':
        print('Type help() for interactive help, or help(object) for help about object')

    elif command == 'copyright':
        print(COPYRIGHT)

    elif command == 'credits':
        print(CREDITS)

    elif command == 'license':
        print('Type license() to see the full license text')

    elif command == 'help()':
        helper = Helper()
        exittype = helper.help_loop()                                                                               # pylint: disable=C0103

        if exittype == 'hard':
            run = False                                                                                             # pylint: disable=C0103

        elif exittype == 'soft':
            continue

    elif command == 'license()':
        print(LICENSE)

    elif command.startswith('help(') & command.endswith(')'):
        helper = Helper(command[5:-1])
        exittype = helper.help_loop()                                                                               # pylint: disable=C0103

        if exittype == 'hard':
            run = False                                                                                             # pylint: disable=C0103

        elif exittype == 'soft':
            continue

    elif command == 'quit':
        print('Type quit() to exit')

    elif command == 'quit()':
        run = False                                                                                                 # pylint: disable=C0103

    else:
        try:
            lexer = Lexer(command)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()

            if not tree:
                continue

            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)

        except (IllegalChar, SyntaxErrorCust, DivisionByZero) as exp:
            print(exp)
