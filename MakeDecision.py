import Node
import Readatributes as RA


def making_decision(DecisionTree, header):
    print('Write example to test')
    usercall = input().split(',')

    cur = DecisionTree
    while not cur.is_leaf():
        # print(cur.get_attribute(), '\n | ')
        # print(' v ')
        stack = cur.get_attribute()
        index = header.index(stack)
        trash = usercall[index]
        if trash.isdigit():
            counter = 0
            for each in cur.get_children():
                if counter < 3:
                    if int(trash) <= each:
                        cur = cur.get_child(each)
                        break
                    counter += 1
                else:
                    cur = cur.get_child(each)
        elif RA.is_float(trash):
            counter = 0
            for each in cur.get_children():
                if counter < 3:
                    if float(trash) <= each:

                        cur = cur.get_child(each)
                        break
                    counter += 1
                else:
                    cur = cur.get_child(each)
        else:
            cur = cur.get_child(trash)
    return cur.get_attribute()
