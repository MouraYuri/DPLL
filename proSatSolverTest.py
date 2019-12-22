from pysat.solvers import Glucose3
import time

def generateFormula(data):
    retorno = Glucose3()
    data = [x.split() for x in data]
    for x in range(len(data)):
        if (data[x][0] == 'p'):
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
                retorno.add_clause(clause)
    return retorno


#data = (open('./CursosEmUmEvento/outTresHoras.txt', 'r')).readlines()
data = (open('./CursosEmUmEvento/outCincoHoras.txt', 'r')).readlines()
#data = (open('in', 'r')).readlines()

clauses = generateFormula(data)

t0 = time.time()
result = clauses.solve()
t1 = time.time()

print('\nResposta Final SatSolver Profissional => {}\n'.format(result))
print('{}\n'.format(clauses.get_model()))
print('Tempo de execução SatSolver Profissional => {}\n'.format(t1-t0))

print('finished')