import ply.lex as lex
from tabulate import tabulate

BlackList = ['WHERE','FROM','SELECT','JOIN',
                 'INNER','FULL','AND','OR','NOT',
                 'LIKE','DELETE','DROP','DELETE',
                 'CREATE','UPDATE','ALTER','IN',
                 'BETWEEN','IF','WHILE']
    
    #String de negación para las palabras reservadas de SQL
BlackString = "("+"\b)|(".join(BlackList)+"\b)"

    #Expresión regular con las palabras reservadas SQL
RES = f'(?!{BlackString})'

token_list = []

tokens = (
    'SELECT',
    'ASTERISK',
    'FROM',
    'WHERE',
    'TABLE',
    'ATTRIBUTE',
    'OPERATOR',
    'SEPARATOR',
    'NUMBER',
    'STRING'
    
)

TABLE = fr'{RES}([A-Z](_?([A-Z0-9]))*)'


t_ASTERISK = r'\b\*\b'
t_FROM = r'\bFROM\b'
t_WHERE = r'\bWHERE\b'
t_TABLE = fr'({TABLE})'
t_ATTRIBUTE = fr'{TABLE}(\.{TABLE})?'
t_OPERATOR = r'(\+|\-|\*|\/|\%|(\sAND\s)|(\sOR\s)|(\<\=?)|(\>\=?)|(\=\=)|(\=)|(\>\<)|(\sLIKE\s))'
t_SEPARATOR = r','
t_NUMBER = r'(\d+(\.\d+)?)'
t_STRING = r"'.*?'"
t_SELECT = r'\bSELECT\b'

def t_error(t):
    if t.value[0] != " ":
        token_list.append(('INVALID',t.value[0],t.lineno,t.lexpos))
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(data):
    token_list.clear()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type,tok.value,tok.lineno,tok.lexpos))
    table = tabulate(token_list,headers=["Tipo","Valor                        ","Ln","Col"],tablefmt='simple',)
    return table








    