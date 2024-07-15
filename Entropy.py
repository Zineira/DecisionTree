import math


def carry(classe, target, atributos, last):
    atributos_incertos = []
    count = 0
    # reset target
    for each in target:
        target[each] = 0

    for each in atributos:
        # uses target to count how many have in that class
        for i in range(len(classe)):
            if classe[i] == each:
                target[last[i]] += 1

        for cada in target:
            if target[cada] > 0:
                count += 1
            target[cada] = 0
        if count == len(target):
            atributos_incertos.append(each)
        count = 0
    return atributos_incertos


def entropy_calculator(organizados, target, atributos, header):
    entropys = []
    k = 0
    last = list(organizados.keys())[-1]

    for i in organizados:
        if not i == last:
            entro = entropy(
                organizados[i], target, atributos[k], organizados[last])
            entropys.append(entro)
            k += 1

    minEntropy = min(entropys)
    minindex = entropys.index(minEntropy)

    return header[minindex], minindex


def entropy(classe, target, atributos, last):
    entro = 0.0
    atribut = []
    for i in range(len(atributos)):
        atr = entropyHelper(classe, target, atributos[i], last)
        atribut.append(atr)
    entro = sum(atribut)

    return entro


def entropyHelper(classe, target, atributo, last):
    entro = 0.0
    numatributos = len(classe)
    total = 0
    for i in range(len(classe)):
        if classe[i] == atributo:
            total += 1
            target[last[i]] += 1

    for each in target:
        if total == 0:
            continue
        else:
            probability = target[each]/total
            if probability == 0:
                entro = 0
                break
            else:
                entro -= probability*math.log2(probability)
            target[each] = 0
    for each in target:
        target[each] = 0
    return (total/numatributos)*entro
