import ply.lex as lex #importing lex module from PLY package for lexical/tokenising
import ply.yacc as yacc #importing yacc module from PLY package for parsing

# Define the list of tokens
tokens = (
    'QUESTION', 'COLON', 'ID', 'NUMBER',
)

# Regular expressions for the ternary operator symbols
t_QUESTION = r'\?'
t_COLON = r':'

# A regular expression for identifiers (IDs)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

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

# Define the grammar rules for the parser
def p_conditional_expression(p):
    '''
    expression : expression QUESTION expression COLON expression
    '''
    print(f"Valid C++ ternary condition:")
    p[0] = p[3] if p[1] else p[5]

#expression can be of ID token type
def p_expression_id(p):
    'expression : ID'
    p[0] = p[1]

#expression can be of NUMBER token type
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

#When it encounters an invalid character
def p_error(p):
    print(f"Syntax error at token '{p.type}'\nInvalid syntax")
    
# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Example C++ ternary conditional expression
cpp_code = input("Enter the expression\n")

# Parse the expression
parser.parse(cpp_code)


