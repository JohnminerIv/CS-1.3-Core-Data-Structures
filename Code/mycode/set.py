from binarytree import BinarySearchTree
from queue import LinkedQueue
import sys


class Setree:
    def __init__(self, ls=None):
        self.tree = BinarySearchTree()
        self.size = 0
        for item in ls:
            self.add(item)

    def add(self, item):
        '''Add an item to the set. O(log(n))'''
        if self.contains(item) is False:
            self.tree.insert(item)
            self._update_size()

    def contains(self, item):
        '''Check if set contains item. O(log(n))'''
        return self.tree.contains(item)

    def remove(self, item):
        '''Remove item from set or ValueError O(log(n))'''
        self.tree.delete(item)
        self._update_size()

    def union(self, nset):
        '''Create a new set with elements of both sets O()'''
        nnset = self.tree
        for item in nset._in_order():
            nnset.add(item)
        return nnset

    def intersection(self, nset):
        '''Create a new set with elements that are in both sets O(n)'''
        items = nset._in_order()
        return Setree([i for i in items if self.contains(i)])

    def is_subset(self, nset):
        '''Check if each item in one set is in another set O(n)'''
        items = nset._in_order()
        for i in items:
            if self.contains(i) is False:
                return False
        return True

    def _in_order(self):
        """returns all of the values in a set in sorted order"""
        return self.tree.items_in_order()

    def _update_size(self):
        """Updates the size."""
        self.size = self.tree.size

    def bad_balance(self):
        print('Previous height:')
        print(self._height())
        queue = LinkedQueue()
        ls = self._in_order()
        self._binary_sorter(ls, queue.enqueue)
        self.tree = BinarySearchTree()
        while queue.front() is not None:
            self.add(ls[queue.dequeue()])
        print('Balanced height:')
        print(self._height())

    def _binary_sorter(self, ls, visit, last=None, left=None, right=None):
        if left is None:
            left, right = 0, len(ls) - 1
        midpoint = left + ((right-left)//2)
        visit(midpoint)
        if midpoint != last:
            self._binary_sorter(ls, visit, midpoint, midpoint + 1, right)
        if midpoint != last:
            self._binary_sorter(ls, visit, midpoint, left, midpoint - 1)

    def _height(self):
        return self.tree.root.height()



def main():
    set = Setree(sys.argv[1:])
    # print(set.size)
    print(set._in_order())
    set.bad_balance()
    print(set._in_order())


if __name__ == '__main__':
    main()
