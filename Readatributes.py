import csv
import numpy as np
import copy
import Entropy


def switchswitch(transpose, dtype):
    smallest = min(transpose)
    biggest = max(transpose)
    if dtype == 'float':
        ranger = round(float((biggest - smallest) / 4), 1)
        small = smallest + ranger
        medium = smallest + ranger * 2
        big = smallest + ranger * 3
        evenbigger = smallest + ranger * 4
    else:
        smallest = int(smallest)
        ranger = int(round((biggest - smallest) / 4, 0))
        small = int(smallest + ranger)
        medium = int(smallest + ranger * 2)
        big = int(smallest + ranger * 3)
        evenbigger = int(smallest + ranger * 4)

    for j in range(len(transpose)):
        if transpose[j] <= small:
            transpose[j] = small
        elif transpose[j] <= medium:
            transpose[j] = medium
        elif transpose[j] <= big:
            transpose[j] = big
        else:
            transpose[j] = evenbigger


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def input_read():

    csvFileName = input(
        "Enter the name of the csv file to build the tree: ") + '.csv'

    file = open(csvFileName)
    csvReader = csv.reader(file)

    header = []
    header = next(csvReader)
    header.pop(0)

    organized = []  # holds the info for the amount of variables
    for row in csvReader:
        organized.append(row)

    attributes = []  # list of the atributes
    results = []  # target values
    data = {}  # dados data
    target = {}  # quantity of the target variables

    for i in range(len(organized)):
        organized[i].pop(0)

    for each in results:
        target[each] = 0

    for r in organized:
        if r[-1] not in results:
            results.append(r[-1])

    transpose = list(np.transpose(organized))

    for i in range(len(transpose)):
        if transpose[i][0].isdigit():
            transpose[i] = [int(element) for element in transpose[i]]
            switchswitch(transpose[i], 'int')
        elif is_float(transpose[i][0]):
            transpose[i] = [float(element) for element in transpose[i]]
            switchswitch(transpose[i], 'float')

    organized = np.transpose(transpose).tolist()

    for i in range(len(transpose)-1):
        attributes.append([])
        for r in transpose[i]:
            if r not in attributes[i]:
                attributes[i].append(r)

    for each in results:
        target[each] = 0

    for i in range(len(header)):
        data[header[i]] = list(transpose[i])

    file.close()
    return data, organized, target, attributes


def num_headers(data):
    return list(data)


def update_data(data, organized, target, attributes, Atr, atrindex):
    # reset do target
    newdata = copy.deepcopy(data)
    newattributes = copy.deepcopy(attributes)
    neworganized = copy.deepcopy(organized)
    for each in target:
        target[each] = 0

    header = num_headers(newdata)
    data_filtred = []
    lines_to_keep = [True for i in range(len(neworganized))]
    last = num_headers(newdata)[-1]

    nextAtr = Entropy.carry(
        newdata[Atr], target, newattributes[atrindex], newdata[last])
    for each in nextAtr:
        for i in range(len(neworganized)):
            if neworganized[i][atrindex] == each:
                lines_to_keep[i] = False

    # Moved this operation out of the previous loop
    for i in range(len(neworganized)):
        neworganized[i].pop(atrindex)

    for i in range(len(neworganized)):
        if not lines_to_keep[i]:
            data_filtred.append(neworganized[i])
    neworganized = data_filtred

    # remove attribute from header
    header.pop(atrindex)

    # remove attribute from data
    del newdata[Atr]

    for each in newdata:
        for j in range(len([newdata[each]])):
            newdata[each][j] = str(newdata[each][j])
        # recreate data based on new organized and header
    transpose = list(np.transpose(neworganized))
    if len(transpose) > 0:
        for i in range(len(header)):
            newdata[header[i]] = list(transpose[i])

    # remove attribute from attributes list
    newattributes.pop(atrindex)
    return newdata, neworganized, target, newattributes, nextAtr
