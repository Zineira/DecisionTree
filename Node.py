class Node:
    def __init__(self, attribute=None):
        self.attribute = attribute
        self.children = {}

    def print_Tree(self, counter=0):
        if self.is_leaf():
            print('    ' * counter, f' "{self.get_attribute()}" ')
        else:
            counter += 1
            print('    ' * counter, self.get_attribute())
            for each in self.children:
                print('     ' * counter, f'[{each}]')
                self.children[each].print_Tree(counter)

    def set_attribute(self, attribute):
        self.attribute = attribute

    def add_child(self, atr_class):
        self.children[atr_class] = None
        sorted(self.children)

    def set_child(self, atr_class, child_node):
        self.children[atr_class] = child_node

    def get_attribute(self):
        return self.attribute

    def get_children(self):
        return list(self.children)

    def get_child(self, attribute):
        return self.children[attribute]

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False
