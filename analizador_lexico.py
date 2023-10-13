import ply.lex as lex
from ply.lex import TOKEN
from tabulate import tabulate

token_list = []

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'RESERVED',
    'TABLE',
    'ATTRIBUTE',
    'OPERATOR',
    'SEPARATOR',
    'NUMBER',
    'STRING'
)

BlackList = ['JOIN','INNER','FULL','NOT',
                 'LIKE','DELETE','DROP','DELETE',
                 'CREATE','UPDATE','ALTER','IN',
                 'BETWEEN','IF','WHILE','FOR']

RES = r"(\b"+r"\b)|(\b".join(BlackList)+r"\b)"

TABLE = fr'([A-Z](_?([A-Z0-9]))*)'

@TOKEN(r'\bSELECT\b')
def t_SELECT(t):
    return t

@TOKEN(r'\bFROM\b')
def t_FROM(t):
    return t

@TOKEN(r'\bWHERE\b')
def t_WHERE(t):
    return t

@TOKEN(RES)
def t_RESERVED(t):
    return t

@TOKEN(fr'{TABLE}\.{TABLE}')
def t_ATTRIBUTE(t):
    return t

@TOKEN(TABLE)
def t_TABLE(t):
    return t

@TOKEN(r'(\+|\-|\*|\/|\%|(\sAND\s)|(\sOR\s)|(\<\=?)|(\>\=?)|(\=\=)|(\=)|(\>\<)|(\sLIKE\s))')
def t_OPERATOR(t):
    return t

@TOKEN(r',')
def t_SEPARATOR(t):
    return t

@TOKEN(r'\d+(\.\d+)?')
def t_NUMBER(t):
    return t

@TOKEN(r"'.*?'")
def t_STRING(t):
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    if not t.value[0] in ['\n',' ']:
        token_list.append(('INVALID',t.value[0],t.lineno,t.lexpos))
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(data):
    token_list.clear()
    lexer.lineno = 0
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type,tok.value,tok.lineno,tok.lexpos))
    table = tabulate(token_list,headers=["Tipo","Valor                        ","Ln","Col"],tablefmt='simple',)
    return table








    