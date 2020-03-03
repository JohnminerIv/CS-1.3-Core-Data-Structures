from binarytree import BinarySearchTree
from queue import LinkedQueue
import sys


class Setree:
    def __init__(self, ls=None):
        self.tree = BinarySearchTree()
        self.size = 0
        if ls is not None:
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
        '''Create a new set with elements of both sets O((m+n)*log(m+n))'''
        return Setree(self.in_order()+nset.in_order())

    def intersection(self, nset):
        '''Create a new set with elements that are in both sets O(min(m,n)*log(n)*log(m))'''
        if self.size > nset.size:
            small = nset
            big = self
        else:
            big = nset
            small = self
        nnset = Setree()
        for item in small.in_order():
            if big.contains(item):
                nnset.add(item)
        return nnset

    def is_subset(self, nset):
        '''Check if each item in one set is in this set O(n*log(n)*log(m))'''
        if self.size < nset.size:
            return False
        items = nset.in_order()
        for i in items:
            if self.contains(i) is False:
                return False
        return True

    def difference(self, nset):
        '''Check for each item in this is not in another set O(m*log(n))'''
        return Setree([i for i in self.in_order() if nset.contains(i) is False])

    def in_order(self):
        """returns all of the values in a set in sorted order O(m)"""
        return self.tree.items_in_order()

    def _update_size(self):
        """Updates the size."""
        self.size = self.tree.size

    def bad_balance(self):
        print('Previous height:')
        print(self._height())
        queue = LinkedQueue()
        ls = self.in_order()
        self._binary_sorter(ls, queue.enqueue)
        self.tree = BinarySearchTree()
        count = 1
        while queue.front() is not None:
            self.add(ls[queue.dequeue()])
            count += 1
        print('Balanced height:')
        print(self._height())
        print(count)

    def _binary_sorter(self, ls, visit, last=None, left=None, right=None):
        if left is None:
            left, right = 0, len(ls) - 1
        midpoint = left + ((right-left)//2)
        if midpoint != last:
            visit(midpoint)
        if midpoint != last:
            self._binary_sorter(ls, visit, midpoint, midpoint + 1, right)
        if midpoint != last:
            self._binary_sorter(ls, visit, midpoint, left, midpoint - 1)

    def _height(self):
        return self.tree.root.height_f()


def main():
    set = Setree(sys.argv[1:])
    # print(set.size)
    print(set.in_order())
    set.bad_balance()
    print(set.in_order())


if __name__ == '__main__':
    main()
