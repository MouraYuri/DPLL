from functools import reduce
def tem_unitaria(clausulas):
    for x in clausulas:
        if len(x) == 1: return True
    return False

def pega_unitaria(clausulas):
    for x in clausulas:
        if len(x) == 1: return x[0]

def simplifica(clausulas):
    valoracao = {}
    while(tem_unitaria(clausulas)):
        literal_unitario = pega_unitaria(clausulas)
        

clausulas = [[1, -3], [2, 3, -1], [-1]]

print(tem_unitaria(clausulas))

simplifica(clausulas)

