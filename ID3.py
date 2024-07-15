from collections import Counter
import Readatributes as RA
import Node
import Entropy
# Define ID3 algorithm


def most_frequent(List):
    counter = Counter(List)
    return max(counter.keys(), key=(lambda k: counter[k]))


def id3(data, organized, target, attributes, nextAtr):
    root = Node.Node()
    header = RA.num_headers(data)
    last = list(data)[-1]

    if len(set(data[last])) == 1:
        root.set_attribute(data[last][0])
        return root
    if len(header) == 0:
        root.set_attribute(most_frequent(data[last]))
        return root
    else:
        if len(nextAtr) == 0:
            whateveryouwant = Node.Node(most_frequent(data[last]))
            root.add_child(whateveryouwant)
        else:
            Atr, atrindex = Entropy.entropy_calculator(
                data, target, attributes, list(data))
            nextAtr = Entropy.carry(
                data[Atr], target, attributes[atrindex], data[last])
            root.set_attribute(Atr)

            for each in attributes[atrindex]:
                root.add_child(each)
                if each not in data[Atr]:
                    whateveryouwant = Node.Node(most_frequent(data[last]))
                    root.set_child(each, whateveryouwant)

                elif Entropy.entropyHelper(data[Atr], target, each, data[last]) == 0:
                    for i in range(len(data[Atr])):
                        if data[Atr][i] == each:
                            class_atr = data[last][i]
                            break
                    whateveryouwant = Node.Node(class_atr)
                    root.set_child(each, whateveryouwant)

                else:

                    if len(nextAtr) > 0:
                        child = Node.Node()
                        # for cada in data:
                        #     print(cada, data[cada])
                        # print()

                        newdata, neworganized, target, newattributes, newnextAtr = RA.update_data(
                            data, organized, target, attributes, Atr, atrindex)

                        child = id3(newdata, neworganized, target,
                                    newattributes, newnextAtr)

                        root.set_child(
                            each, child)

    return root
