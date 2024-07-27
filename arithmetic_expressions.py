import ply.lex as lex #importing lex module from PLY package for lexical/tokenising
import ply.yacc as yacc #importing yacc module from PLY package for parsing

# Define the list of tokens
tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# A regular expression for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  #number should be of python integer type
    return t

# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)  # print the offending character and skip ahead one character by calling t.lexer.skip(1).

# Define the precedence and associativity of operators
precedence = (
    ('left', 'PLUS', 'MINUS'),    #left associativity
    ('left', 'TIMES', 'DIVIDE'),  #left associativity
)

# Define the grammar rules for the parser
def p_expression_binop(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

    print("VALID C++ arithmetic expression\n")

#expression can be between parenthesis
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

#expression can be of NUMBER token type
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

#When it encounters an invalid character
def p_error(p):
    print(f"Syntax error at token {p.type}")
    print("INVALID SYNTAX")


# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Input C++ arithmetic expression
cpp_expression = input("Enter the expression\n")

# Parse the expression
parser.parse(cpp_expression)

