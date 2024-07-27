import ply.lex as lex  #importing lex module from PLY package for lexical/tokenising
import ply.yacc as yacc #importing yacc module from PLY package for parsing


# Define the list of tokens
tokens = (
    'IF', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'ID',
)

# Define a simple regular expression for the "if" keyword
def t_IF(t):
    r'if'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9_>_<_=_"_;]*'
    return t

# Regular expressions for parentheses, braces, and semicolon
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'


# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)  # print the offending character and skip ahead one character by calling t.lexer.skip(1).

# Define the grammar rules for the parser
def p_if_statement(p):
    '''
    statement : IF LPAREN expression RPAREN LBRACE expression RBRACE
    '''
    print("VALID C++ if statement detected")

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''

# Define an empty expression
def p_expression_empty(p):
    'expression : '
    pass

#Defining an expression of ID token type
def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

#When it encounters an invalid character
def p_error(p):
    print(f"Syntax error at token '{p.type}'\nINVALID SYNTAX")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Input C++ if expression
cpp_expression = input("Enter the expression\n")

# Parse the expression
parser.parse(cpp_expression)

