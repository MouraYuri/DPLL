

conectivos = ['&', '~', '||', '=>', '<=>']
inter = {
    't': False,
    'x' : False,
    'a' : False
}

formula = [[['t'], ['&'], [['~'], ['x']]], ['||'], ['a']]
atomicos = ['t', 'x', 'a']
#sentence = open('text1', 'r')
#sentence = sentence.readlines()

#print(sentence[0].split(' '))

#form = sentence[0].split(' ')

def valoracao(form, interpretacao):
    if (len(form) == 1):
        return interpretacao[form[0]]
    if (len(form)==3):
        if (form[1]==['||']):
            return valoracao(form[0],interpretacao) or valoracao(form[2],interpretacao)
        if (form[1] == ['&']):
            return valoracao(form[0],interpretacao) and valoracao(form[2],interpretacao)
        if(form[1] == ['=>']):
            return (not valoracao(form[0], interpretacao)) or valoracao(form[2],interpretacao)
    if (len(form)==2):
        return not valoracao(form[1],interpretacao)




