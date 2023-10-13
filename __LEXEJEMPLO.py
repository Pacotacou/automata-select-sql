import ply.lex as lex

# Lista de nombres de tokens. Esto es siempre requerido
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
)

# Reglas de expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

# Una regla de expresión regular con algunas acciones de código
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value) 
    return t

# Definir una regla para poder rastrear números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Una cadena que contiene caracteres ignorados (espacios y tabulaciones)
t_ignore  = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Probarlo
data = '''
3 + 4 * 10
  + -20 *2 a
'''

lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
