def allInFiveHours(data):
    #variáveis
    data, atomsGroup, restrictions = [x.split() for x in data], [], []
    hashtagIndex = data.index(['#'])

    #removendo as duplicatas
    [data.remove(x) for x in data[hashtagIndex+1:] if x[::-1] in data]

    print('data => {}\n'.format(data))

    #criando as atomicas
    for x in data:
        if (x != ['#']):
            atomsGroup.append([int(x[0]+'1'), int(x[0]+'2'), int(x[0]+'3'), int(x[0]+'4'), int(x[0]+'5')])
            continue
        break

    print('atomsGroup => {}\n'.format(atomsGroup))


    #criando as restrições
    [[restrictions.append([atomsGroup[int(x[0])-1][y]*-1, atomsGroup[int(x[1])-1][y]*-1]) for y in range(5)] for x in data[hashtagIndex+1:]]
    for x in atomsGroup:
        #gambiarra abaixo
        restrictions.append([int(x[0])*-1, int(x[1])*-1])
        restrictions.append([int(x[0])*-1, int(x[2])*-1])
        restrictions.append([int(x[0])*-1, int(x[3])*-1])
        restrictions.append([int(x[0])*-1, int(x[4])*-1])

        restrictions.append([int(x[1])*-1, int(x[0])*-1])
        restrictions.append([int(x[1])*-1, int(x[2])*-1])
        restrictions.append([int(x[1])*-1, int(x[3])*-1])
        restrictions.append([int(x[1])*-1, int(x[4])*-1])

        restrictions.append([int(x[2])*-1, int(x[0])*-1])
        restrictions.append([int(x[2])*-1, int(x[1])*-1])
        restrictions.append([int(x[2])*-1, int(x[3])*-1])
        restrictions.append([int(x[2])*-1, int(x[4])*-1])

    [restrictions.append(x) for x in atomsGroup]

    print("Restrições => {}\n".format(restrictions))

    #escrevendo a saída
    outFile = open('./CursosEmUmEvento/outCincoHoras.txt', 'w')
    outFile.write("c comentario\np cnf {} {}\n".format(len(atomsGroup)*5, len(restrictions)))
    [outFile.write("{} {} 0\n".format(x[0],x[1])) for x in restrictions[:-len(atomsGroup)]]
    #[outFile.write("{} {}\n".format(x[0],x[1])) for x in restrictions[:-len(atomsGroup)]] #para testar no SAT SOLVER DA UFPR
    [outFile.write("{} {} {} 0\n".format(x[0], x[1], x[2])) for x in restrictions[-len(atomsGroup):]]
    outFile.close()

allInFiveHours(open('./CursosEmUmEvento/inTresHoras', 'r').readlines())


#Resposta Final => {21: False, 22: False, 23: True, 13: False, 33: False, 43: False, 41: False, 42: True, 32: False, 31: True, 11: False, 12: True}