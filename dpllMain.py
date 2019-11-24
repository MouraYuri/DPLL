
def generateFormula(data):
    atoms, clauses = [], []
    data = [x.split() for x in data]
    for x in range(len(data)):
        if (data[x][0] == 'p'):
            [atoms.append('p'+ str(y+1)) for y in range(int(data[x][2]))]
            for y in range(int(data[x][3])):
                clause = []
                for z in range(len(data[x+y+1])):
                    #x -> Linha onde está o p
                    #y -> qtd de clausulas que somada com x + 1 me dá as linhas abaixo de p
                    if (int(data[x+y+1][z])<0):
                        #clause.append([['~'],[atoms[(int(data[x+y+1][z])*-1)-1]]])
                        #clause.append(['||'])
                        #=====CÓDIGO ACIMA CONTRÓI A FÓRMULA=====
                        clause.append([['~'], [atoms[(int(data[x+y+1][z])*-1)-1]]])

                    if (int(data[x+y+1][z])>0):
                        #clause.append([atoms[(int(data[x+y+1][z]))-1]])
                        #clause.append(['||'])
                        #=====CÓDIGO ACIMA CONTRÓI A FÓRMULA=====
                        clause.append([atoms[(int(data[x + y + 1][z])) - 1]])

                # [ [ ['~'], ['p3'] ], ['||'], ['p1'] ]
                #clauses.append(clause[:-1]) #-1 porque ele fica adicionando um 'ou' a mais
                clauses.append(clause)  #o de cima é para contrução da fórmula
    return clauses

def dpll(clauses):
    



data = (open('in', 'r')).readlines()

clauses = generateFormula(data)
print(clauses)
print('finished')