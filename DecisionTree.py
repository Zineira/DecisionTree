import Readatributes as RA
import ID3
import Node
import MakeDecision as MD

DecisionTree = Node.Node()

while True:
    print('1: Create a new DecisionTree | 2: Make a decision | 3: Print the Tree |"4": Quit')
    var = input()

    if var == '1':
        data, organized, target, attributes = RA.input_read()
        DecisionTree = ID3.id3(data, organized, target, attributes, ['Bait'])
        print('#####DONE#####')
    elif var == '2':
        if (len(data) > 0):
            header = RA.num_headers(data)[:-1]
            ans = MD.making_decision(DecisionTree, header)
            print(ans)
    elif var == '3':
        DecisionTree.print_Tree()
    else:
        break
