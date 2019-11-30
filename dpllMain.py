from simplifica import simplifica
def generateFormula(data):
    atoms, clauses = [], []
    data = [x.split() for x in data]
    for x in range(len(data)):
        if (data[x][0] == 'p'):
            [atoms.append('p'+ str(y+1)) for y in range(int(data[x][2]))]
            for y in range(int(data[x][3])):
                clause = []
                for z in range(len(data[x+y+1])):
                    # =========================================
                    #x -> Linha onde está o p
                    #y -> qtd de clausulas que somada com x + 1 me dá as linhas abaixo de p
                    if (int(data[x+y+1][z])<0):
                        #clause.append([['~'],[atoms[(int(data[x+y+1][z])*-1)-1]]])
                        #clause.append(['||'])
                        #=====CÓDIGO ACIMA CONTRÓI A FÓRMULA=====

                        #=========================================
                        #clause.append([['~'], [atoms[(int(data[x+y+1][z])*-1)-1]]])
                        # =====CÓDIGO ACIMA DEIXA TUDO NA FORMA CLAUSAL=====


                        clause.append((int(data[x + y + 1][z])))
                        

                    if (int(data[x+y+1][z])>0):
                        #=========================================
                        #clause.append([atoms[(int(data[x+y+1][z]))-1]])
                        #clause.append(['||'])
                        #=====CÓDIGO ACIMA CONTRÓI A FÓRMULA=====

                        # =========================================
                        #clause.append([atoms[(int(data[x + y + 1][z])) - 1]])
                        # =====CÓDIGO ACIMA DEIXA TUDO NA FORMA CLAUSAL=====

                        clause.append((int(data[x + y + 1][z])))


                #clauses.append(clause[:-1]) #-1 porque ele fica adicionando um 'ou' a mais
                clauses.append(clause)  #o de cima é para construção da fórmula
    return clauses

def pega_literal(clausulas):
    return clausulas[0][0]


def dpll(clausulas, valoracao):
    clausulas, valoracao2 = simplifica(clausulas)
    valoracao.update(valoracao2) #concatena 2 dicionários
    if (len([clausula for clausula in clausulas if (len(clausula)==0)])>0) : return False #se existir uma clausula vazia
    if (len(clausulas)==0) : return valoracao
    literal = pega_literal(clausulas)
    clausulas1, clausulas2 = clausulas + [[literal]], clausulas + [[-1*literal]]
    res = dpll(clausulas1, valoracao)
    if (res != False) : return res
    return dpll(clausulas2, valoracao)



data = (open('in', 'r')).readlines()

clauses = generateFormula(data)
#clauses = [[1, -3], [2, 3, -1]]

print("Resposta Final => {}\n".format(dpll(clauses, {})))
print('finished')