from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


def tokenize(code):
    keywords_cpp = {'auto', 'break', 'case', 'char',
                    'const', 'continue', 'default', 'do',
                    'double', 'else', 'enum', 'extern',
                    'float', 'for', 'goto', 'if',
                    'int', 'long', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static',
                    'struct', 'switch', 'typedef', 'union',
                    'unsigned', 'void', 'volatile', 'while'}
 
    token_specification = [
        ('assignment_operator', r'=|(/=)|\*='), 
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1
    line_start = 0
    
	
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        
        yield Token(kind, value, line_num, column)


def main():
    
    for token in tokenize(add_the_code_here):
        print(token)


if __name__ == '__main__':
    main()