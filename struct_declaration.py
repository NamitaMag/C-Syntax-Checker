import ply.lex as lex  #importing lex module from PLY package for lexical/tokenising
import ply.yacc as yacc #importing yacc module from PLY package for parsing

# Define the list of tokens
tokens = (
    'STRUCT', 'ID', 'LBRACE', 'RBRACE', 'SEMICOLON',
)

# Define a simple regular expression for the "struct" keyword
def t_STRUCT(t):
    r'struct'
    return t

# Regular expressions for braces and semicolon
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# A regular expression for identifiers (IDs)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Ignore whitespace , newline and tabs
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)  # print the offending character and skip ahead one character by calling t.lexer.skip(1).

# Define the grammar rules for the parser
def p_struct_declaration(p):
    '''
    declaration : STRUCT ID LBRACE RBRACE SEMICOLON
    '''
    print(f"VALID Structure Declaration: '{p[2]}'")

#When it encounters an invalid character
def p_error(p):
    print(f"Syntax error at token '{p.type}'\nINVALID SYNTAX")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Example C++ structure declaration
cpp_code = input("Enter the expression\n")

# Tokenize and parse the code
lexer.input(cpp_code)
for token in lexer:
    print(token)  #prints the attributes (token.type, token.value, token.lineno, and token.lexpos) 
                  #of LexToken object for each token

# Parse the expression
parser.parse(cpp_code)
