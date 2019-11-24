from consequencia import consequencia

formula = [['p1'], ['||'], [['~'], ['p1']]]

def satisfazivel(formula):
    aux = [['~']]
    aux.append(formula)
    return (consequencia([], aux) == False)

print(satisfazivel(formula))