import re

#Función para verificar consultas SQL
def isValidSql(str):
    #Lista de palabras reservadas de SQL
    BlackList = ['WHERE','FROM','SELECT','JOIN',
                 'INNER','FULL','AND','OR','NOT',
                 'LIKE','DELETE','DROP','DELETE',
                 'CREATE','UPDATE','ALTER','IN',
                 'BETWEEN','IF','WHILE']
    
    #String de negación para las palabras reservadas de SQL
    BlackString = "("+"\W)|(".join(BlackList)+"\W)"

    #Expresión regular con las palabras reservadas SQL
    RES = f'(?!{BlackString})'

    #Variables
    TABLE = f'({RES}([A-Z](\_?([A-Z]|\d))*))'
    ATRIB = f'(({TABLE}(\.{TABLE})?))'
    VALUE = '((\d+(\.\d+)?)|(\'.*\'))'
    OP = '(\+|\-|\*|\/|\%|(\sAND\s)|(\sOR\s)|(\<\=?)|(\>\=?)|(\=\=)|(\=)|(\<\>)|(\sLIKE\s))'

    #Atributo o Valor, puede ir con cero, uno o varios NOT al principio
    ATRIBVAL =  f'((\s*NOT\s+)*({ATRIB}|{VALUE}))'

    #Construcción de la expresión regular
    RegEx = f'\s*SELECT\s+(\*|{ATRIBVAL}(\s*\,\s*{ATRIBVAL})*)'
    RegEx += f'\s+FROM\s+{TABLE}(\s*,\s*{TABLE})*\s*'
    RegEx += f'(\s+WHERE\s+{ATRIBVAL}(\s*{OP}\s*{ATRIBVAL})*)?\s*'

    #Retornar el resultado
    return re.fullmatch(RegEx,str)

    
