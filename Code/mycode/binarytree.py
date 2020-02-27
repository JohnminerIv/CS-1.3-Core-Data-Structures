#!python
from queue import LinkedQueue
import random
class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: Omega(1) if leaf O(n) if root"""
        # TODO: Check if left child has a value and if so calculate its height
        if self.left is not None:
            left_val = self.left.height() + 1
        else:
            left_val = 0
        # TODO: Check if right child has a value and if so calculate its height
        if self.right is not None:
            right_val = self.right.height() + 1
        else:
            right_val = 0
        return max(left_val, right_val)
        # Return one more than the greater of the left height and right height


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: Theta(n) All conditions"""
        # TODO: Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: Omega(1) if item == self.root.data
        Worst case running time: O(n) if item is in a leaf in a completely
        unbalanced tree"""
        # Find a node with the given item, if any
        if self.root is None:
            return False
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: Omega(1) if item == self.root.data
        Worst case running time: O(n) if item is in a leaf in a completely
        unbalanced tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: Omega(1) if no items in tree
        Worst case running time: O(n) if item to be inserted is a leaf in a completely
        unbalanced tree"""
        # Handle the case where the tree is emp
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
        # Find the parent node of where the given item should be inserted
        else:
            parent = self._find_parent_node_recursive(item, self.root)
            # TODO: Check if the given item should be inserted left of parent node
            if item < parent.data:
                # TODO: Create a new node and set the parent's left child
                parent.left = BinaryTreeNode(item)
            # TODO: Check if the given item should be inserted right of parent node
            elif item > parent.data:
                # TODO: Create a new node and set the parent's right child
                parent.right = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: Omega(1) item is first in tree
        Worst case running time: O(n) item is a leaf in unbalanced tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: Omega(1) item is root
        Worst case running time: O(n) completely unbalanced tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self. _find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self. _find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: Omega(1) item is root
        Worst case running time: O(n) item is leaf in completely unbalanced tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = parent.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = parent.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # TODO: Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)  # Hint: Remember to update the parent parameter

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: Omega(1) item is the only item in the tree
        Worst case running time: O(n) item is a leaf in a tree that is
        completely unbalanced"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        parent = self._find_parent_node_recursive(item, self.root)
        node = None
        direction = None
        if parent is not None:
            if parent.left is not None:
                if parent.left.data == item:
                    node = parent.left
                    direction = 'left'
            if parent.right is not None:
                if parent.right.data == item:
                    node = parent.right
                    direction = 'right'
        else:
            if self.root is not None:
                if self.root.data == item:
                    node = self.root
        if node is None:
            raise ValueError
        elif node.left is None and node.right is None:
            self.no_childs(parent, direction, item)
        elif node.left is not None and node.right is not None:
            self.two_childs(parent, direction, item)
        else:
            if node.left is not None:
                self.one_childs(parent, direction, item)
            else:
                self.one_childs(parent, direction, item)
        if self.size == 0:
            self.root = None

    def no_childs(self, parent, direction, item):
        if parent is not None:
            if direction == 'left':
                parent.left = None
                self.size -= 1
            elif direction == 'right':
                parent.right = None
                self.size -= 1
            else:
                raise ValueError
        else:
            if item == self.root.data:
                self.root.data = None
                self.size -= 1
            else:
                raise ValueError

    def one_childs(self, parent, direction, item):
        if parent is not None:
            if direction == 'left':
                if parent.left.left is not None:
                    next_node = parent.left.left
                    parent.left.left = None
                    parent.left = next_node
                    self.size -= 1
                else:
                    next_node = parent.left.right
                    parent.left.right = None
                    parent.left = next_node
                    self.size -= 1
            elif direction == 'right':
                if parent.right.left is not None:
                    next_node = parent.right.left
                    parent.right.left = None
                    parent.right = next_node
                    self.size -= 1
                else:
                    next_node = parent.right.right
                    parent.right.right = None
                    parent.right = next_node
                    self.size -= 1
            else:
                raise ValueError
        else:
            if item == self.root.data:
                if self.root.left is not None:
                    next_node = self.root.left
                    self.root.left = None
                    self.root = next_node
                    self.size -= 1
                else:
                    next_node = self.root.right
                    self.root.right = None
                    self.root = next_node
                    self.size -= 1
            else:
                raise ValueError

    def two_childs(self, parent, direction, item):
        if parent is not None:
            if direction == 'left':
                successor = self.find_successor(parent.left)
                self.delete(successor.data)
                successor.left = parent.left.left
                successor.right = parent.left.right
                parent.left.left = None
                parent.left.right = None
                parent.left = successor
            elif direction == 'right':
                successor = self.find_successor(parent.right)
                self.delete(successor.data)
                successor.left = parent.right.left
                successor.right = parent.right.right
                parent.right.left = None
                parent.right.right = None
                parent.right = successor
            else:
                raise ValueError
        else:
            if item == self.root.data:
                successor = self.find_successor(self.root)
                # print(successor)
                self.delete(successor.data)
                successor.left = self.root.left
                successor.right = self.root.right
                self.root.right = None
                self.root.left = None
                self.root = successor
            else:
                raise ValueError

    def find_successor(self, node):
        new_node = node.left
        parent = None
        while new_node is not None:
            parent = new_node
            new_node = new_node.right
        return parent

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: Theta(n) must visit every node
        Memory usage: Theta(l) l beign the height of root node"""
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: Theta(n) must visit every node
        Memory usage: Theta(l) l beign the height of root node"""
        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: Theta(n) must visit every node
        Memory usage: Theta(l) l beign the height of root node"""
        # TODO: Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: Theta(n) must visit every node
        Memory usage: Theta((widest level)) if a level has 100 nodes we need to
        enqueue all of them."""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # TODO: Enqueue given starting node
        queue.enqueue(start_node)
        # TODO: Loop until queue is empty
        while queue.is_empty() is False:
            # TODO: Dequeue node at front of queue
            node = queue.dequeue()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]

    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    items_l, items = [], []
    for i in range(2000):
        items_l.append(i)

    items.append(random.choices(items_l, k=200))
    # print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        # print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    # for item in items:
    #     result = tree.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = tree.search(item)
    # print('search({}): {}'.format(item, result))

    # print('\nTraversing items:')
    # print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    # print('items level-order: {}'.format(tree.items_level_order()))
    print('delete random items: ')
    try:
        for i in range(len(items)):
            item = random.choice(items)
            items.remove(item)
            # print(f'Deleted item: {item}')
            # print(f'root{tree.root}')
            tree.delete(item)
            # print('items in-order:    {}'.format(tree.items_in_order()))
    except ValueError:
        pass
    print(tree)


if __name__ == '__main__':
    test_binary_search_tree()
