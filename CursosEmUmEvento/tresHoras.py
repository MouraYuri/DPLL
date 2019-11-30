def allInThreeHours(data):
    #variáveis
    data, atomsGroup, restrictions = [x.split() for x in data], [], []
    hashtagIndex = data.index(['#'])

    #removendo as duplicatas
    [data.remove(x) for x in data[hashtagIndex+1:] if x[::-1] in data]

    print('data => {}\n'.format(data))

    #criando as atomicas
    for x in data:
        if (x != ['#']):
            atomsGroup.append([int(x[0]+'1'), int(x[0]+'2'), int(x[0]+'3')])
            continue
        break

    print('atomsGroup => {}\n'.format(atomsGroup))

    #criando as restrições
    [[restrictions.append([atomsGroup[int(x[0])-1][y]*-1, atomsGroup[int(x[1])-1][y]*-1]) for y in range(3)] for x in data[hashtagIndex+1:]]
    print(restrictions)

    #escrevendo a saída
    outFile = open('outTresHoras.txt', 'w')
    outFile.write("c comentario\np cnf {} {}\n".format(len(atomsGroup)*3, len(restrictions)))
    [outFile.write("{} {} 0\n".format(x[0],x[1])) for x in restrictions]
    outFile.close()

allInThreeHours(open('inTresHoras', 'r').readlines())
