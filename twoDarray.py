import ply.lex as lex  #importing lex module from PLY package for lexical/tokenising
import ply.yacc as yacc #importing yacc module from PLY package for parsing

# Define the list of tokens
tokens = (
    'INT','FLOAT', 'ID', 'LBRACKET', 'RBRACKET', 'SEMICOLON','NUMBER'
)

# A regular expression for int
def t_INT(t):
    r'int'
    return t

# A regular expression for float
def t_FLOAT(t):
    r'float'
    return t

# Regular expressions for brackets and semicolon
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'

# A regular expression for identifiers (IDs)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# A regular expression for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore whitespace and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)  # print the offending character and skip ahead one character by calling t.lexer.skip(1).

# Define the grammar rules for the parser
def p_array_declaration(p):
    '''
    declaration : INT ID LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET SEMICOLON    
                | FLOAT ID LBRACKET NUMBER RBRACKET LBRACKET NUMBER RBRACKET SEMICOLON
    '''
    array_type = p[1]     #datatype of 2d array
    array_name = p[2]     #name of 2d array
    array_size_1 = p[4]   #row size 
    array_size_2 = p[7]   #column size
    array_size_3 = p[9]   #semicolon
    print(f"VALID C++ 2D Array Declaration: {array_type} {array_name}[{array_size_1}][{array_size_2}]{array_size_3}")

#when it encounters an invalid character
def p_error(p):
    print(f"Syntax error at token '{p.type}'\nINVALID SYNTAX")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Example C++ 2D array declaration
cpp_code = input("Enter the expression\n")

# Tokenize and parse the code
lexer.input(cpp_code)
for token in lexer:
    print(token)  #prints the attributes (token.type, token.value, token.lineno, and token.lexpos) 
                  #of LexToken object for each token

parser.parse(cpp_code)
