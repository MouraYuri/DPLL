from functools import reduce
def tem_unitaria(clausulas):
    for x in clausulas:
        if len(x) == 1: return True
    return False

def pega_unitaria(clausulas):
    for x in clausulas:
        if len(x) == 1: return x[0]

def atualiza(clausulas, literal_unitario):
    clausulas = [clausula for clausula in clausulas if (literal_unitario not in clausula)] #cria uma nova lista onde os elementos não tem o literal_unitario
    for c in range(len(clausulas)):
        if (literal_unitario*-1 in clausulas[c]) : clausulas[c].remove(literal_unitario*-1)
    return clausulas


def simplifica(clausulas):
    valoracao = {}
    while(tem_unitaria(clausulas)):
        literal_unitario = pega_unitaria(clausulas)
        if literal_unitario <0:
            valoracao[literal_unitario*-1] = False
        else:
            valoracao[literal_unitario] = True
        clausulas = atualiza(clausulas, literal_unitario)
    return [clausulas, valoracao]


