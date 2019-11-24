from atomicas import atom
from qtdAtomicas import qtdAtom
from valoracao import valoracao

conectivos = ['&', '~', '||', '=>', '<=>']


#Tem que retornar True
#premissas = [[[['c'], ['&'], [['~'], ['g']]], ['=>'], ['m']], ['c'], [['~'], ['m']]]
#formula = ['g']
#

#Tem que retornar False
#premissas = [[['p'], ['=>'], [['q'], ['=>'], ['r']]]]
#formula = [['p'], ['=>'], [['r'], ['=>'], ['q']]]
#

premissas = [[['p'], ['||'], ['q']], [['~'], ['p']]]
formula = [['~'], ['q']]


def consequencia(premissas, formula):
    atomicas = atom(formula)
    for premissa in premissas:
        atomicas = atomicas + atom(premissa)
    interpretacao = {}
    return tabela_consequencia(premissas, formula, atomicas, interpretacao)

def tabela_consequencia(premissas, formula, atomicas , interpretacao):
    if (len(atomicas)==0):
        if (valoracao(formula, interpretacao)):
            return True
        valor_premissa = True
        for premissa in premissas:
            valor_premissa = valor_premissa and valoracao(premissa, interpretacao)
        if valor_premissa:
            return False
        return True
    #Grandes chances de dar bucho abaixo
    atomica = atomicas[0]
    atomicas = atomicas[1:]
    interpretacao1 = {
        atomica: True
    }
    interpretacao1.update(interpretacao)

    interpretacao2 = {
        atomica:False
    }
    interpretacao2.update(interpretacao)
    return tabela_consequencia(premissas, formula, atomicas, interpretacao1) and tabela_consequencia(premissas, formula, atomicas, interpretacao2)

print(consequencia(premissas, formula))






