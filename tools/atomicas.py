atomicas = ['c', 'g', 'm']
formula = [[['c'], ['&'], [['~'], ['g']]], ['=>'], ['m']]


#Retorna as atomicas
def atom(A):
    if (len(A) == 1):
        return [A[0]]
    if (len(A)==3):
        return atom(A[0]) + atom(A[2])
    if (len(A)==2):
        return atom(A[1])
