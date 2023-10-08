import re

def isValidSql(str):
    #RES = f'((?!WHERE\s+|FROM\s+|SELECT\s+|JOIN\s+|INNER\s+|FULL\s+))'
    BlackList = ['WHERE','FROM','SELECT','JOIN',
                 'INNER','FULL','AND','OR','NOT']
    BlackString = "\s+|".join(BlackList)+"\s+"
    RES = f'((?!{BlackString}))'
    
    TABLE = f'{RES}\s*([A-Z](\_?([A-Z]|\d))*)'
    ATRIB = f'{RES}\s*({TABLE}(\.{TABLE})?)'
    VALUE = "((\d+(\.\d+)?) | ('(\w|\s)*') )"
    OP = '(\+|\-|\*|\/|\%|(\sAND\s)|(\sOR\s)|(\<=?)|(\>=?)|(\=\=))'

    #ATRIBVAL = f'({ATRIB}|{VALUE})'
    ATRIBVAL =  f'((\s*NOT\s+)*({ATRIB}|{VALUE}))'

    RegEx = f'SELECT\s+(\*|{ATRIB}(\s*\,\s*{ATRIB})*)'
    RegEx += f'\s+FROM\s+{TABLE}(\s*,\s*{TABLE})*\s*'
    RegEx += f'(\s+WHERE\s+(NOT\s+)*{ATRIBVAL}(\s*{OP}\s*{ATRIBVAL})*)?\s*'

    return re.fullmatch(RegEx,str)

    
