atomicas = ['c', 'g', 'm']
formula = [[['c'], ['&'], [['~'], ['g']]], ['=>'], ['m']]


#Retorna a quantidade de atomicas
def qtdAtom(A):
    if (len(A) == 1):
        return 1
    if (len(A)==3):
        return qtdAtom(A[0]) + qtdAtom(A[2])
    if (len(A)==2):
        return qtdAtom(A[1])
