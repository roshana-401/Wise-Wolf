import ply.lex as lex
from tabulate import tabulate
import os

# File reading section
file_path = os.path.join(os.path.dirname(__file__), "WiseWolf.hp7")

if os.path.exists(file_path):
    with open(file_path, "r",encoding="utf-8") as file_object:
        data = file_object.read()
else:
    print(f"File '{file_path}' not found.")

# tokens
tokens=(
    'COMMENT','STRING','BOOLEAN_TYPE','PLUS_EQ','MINUS_EQ','INT_TYPE','BOOLEAN','ID','SEMICOLON','NUMBER',
    'PRINT','LPAREN','RPAREN','COMMA','LBRACE','RBRACE','RETURN','PLUS','MINUS','TIMES',
    'DIVIDE','MOD','AND','OR','QUESTIONMARK','NOT','ASSIGN','EQUAL','NOT_EQUAL','LT',
    'LTE','GT','GTE','NULL_TYPE','STRING_TYPE','LOOP','BEGIN','END','IF','ELSE','NRP'
)

# Regular expression rules for tokens

t_STRING_TYPE=r'string'
t_INT_TYPE=r'int'
t_BOOLEAN_TYPE=r'boolean'
t_SEMICOLON=r';'
t_PRINT=r'print'
t_PLUS_EQ=r'\+='
t_MINUS_EQ=r'-='
t_LPAREN=r'\('
t_RPAREN=r'\)'
t_COMMA=r','
t_LBRACE=r'{'
t_RBRACE=r'}'
t_RETURN=r'matin'
t_PLUS=r'\+'
t_MINUS=r'-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_MOD=r'%'
t_AND=r'&&'
t_OR=r'\|\|'
t_QUESTIONMARK=r'\?'
t_NOT=r'!'
t_EQUAL=r'=='
t_ASSIGN=r'='
t_NOT_EQUAL=r'!='
t_GTE=r'=\s*>'
t_GT=r'>'
t_NULL_TYPE=r'null'
t_LOOP=r'while'
t_BEGIN=r'az'
t_END=r'morteza'
t_IF=r'if'
t_ELSE=r'else'
t_NRP=r'nrp'
t_LTE=r'<\s*='
t_LT= r'<'
t_STRING=r'".*"'

t_ignore  = ' \t'

def t_COMMENT(t):
    #Sentences that start with <sourin and end with sourin> is comment
    r'<sourin.*sourin>'
    # This function doesn't do anything besides matching the comment pattern.
    return None

def t_BOOLEAN(t):
    #boolean value is true or false
    r'(true|false)'
    return t

def t_ID(t):
    #A word containing uppercase and lowercase letters that can start with (_)and also end with numbers or uppercase and lowercase letters and (_)
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    keywords={
        'string':'STRING_TYPE',
        'int':'INT_TYPE',
        'boolean':'BOOLEAN_TYPE',
        'print':'PRINT',
        'matin':'RETURN',
        'null':'NULL_TYPE',
        'while':'LOOP',
        'az':'BEGIN',
        'morteza':'END',
        'if':'IF',
        'else':'ELSE',
        'nrp':'NRP'
    }
    #It goes into the dictionary, if it doesn't find a key with this word, it sets its ID token
    t.type=keywords.get(t.value,'ID')
    return t

def t_NUMBER(t):
    #If it contains at least one number between 0 and 9
    r'[0-9]+'
    #Converts a numeric value to a real numeric type
    t.value=int(t.value)
    return t

def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
lexer = lex.lex()

# Give the lexer some input
lexer.input(data)


number_of_row=1
# Array for information in table
data = [
    ["Column Number","Line Number", "Word", "Token"]
]
def find_column(lexer, token):
    line_start = lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

while True:
    tok = lexer.token()
    if not tok:
        break
    column_number = find_column(lexer, tok)
    data.append([column_number, tok.lineno, tok.value, tok.type])
    number_of_row += 1 

table_format = "grid"
# create table
table = tabulate(data, headers="firstrow", tablefmt=table_format,numalign="center")
# print table
print(table)
