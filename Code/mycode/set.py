from binarytree import BinarySearchTree
import sys


class Setree:
    def __init__(self, ls=None):
        self.tree = BinarySearchTree()
        for item in ls:
            self.add(item)

    def add(self, item):
        if self.contains(item) is False:
            self.tree.insert(item)

    def contains(self, item):
        return self.tree.contains(item)

    def remove(self, item):
        self.tree.delete(item)

    def union(self, nset):
        return Setree(self.in_order() + nset.in_order())

    def intersection(self, nset):
        items = nset.in_order()
        return Setree([i for i in items if self.contains(i)])

    def is_subset(self, nset):
        items = nset.in_order()
        for i in items:
            if self.contains(i) is False:
                return False
        return True

    def in_order(self):
        return self.tree.items_in_order()

    def size(self):
        return self.tree.size


def main():
    set = Setree(sys.argv[1:])
    print(set.size())
    print(set.in_order())


if __name__ == '__main__':
    main()
