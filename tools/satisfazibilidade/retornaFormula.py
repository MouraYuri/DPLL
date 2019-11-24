frases = open('frases', 'r')
frases = frases.readlines()
print("frases do readlines => {}\n".format(frases))

'''
    True se o professor ficar pela manhã
    False se o professor ficar pela tarde
    & Equivale ao operador AND
    || Equivale ao operador OR
'''

def retornaFormula(frases):
    formulaRetorno = ""
    for x in frases:
        x = x.split(' ')
        #print(x)
        if (len(x) == 2):
            x[1] = x[1].rstrip()
            if (x[1] == 'manha'):
                formulaRetorno = formulaRetorno + '['+ x[0]+']' + ' & '
            else:
                formulaRetorno = formulaRetorno + '[~'+ x[0]+']' + ' & '
        if (len(x)>2):
            x[2] = x[2].rstrip()
            formulaRetorno = formulaRetorno + '[[~' + x[0] + ' & ' + x[2] + '] || [' + x[0] + ' & ' + '~' + x[2] + ']] '
    return formulaRetorno

print(retornaFormula(frases))