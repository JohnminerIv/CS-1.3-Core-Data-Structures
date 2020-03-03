#!python

from binarytree_singlely import BinarySearchTree, Node
import unittest


class BinaryTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = Node(Node(data))
        assert node.data_f() is data
        assert node.left() is None
        assert node.right() is None

    def test_is_leaf(self):
        # Create node with no children
        node = Node(Node(2))
        assert node.is_leaf() is True
        # Attach left child node
        node.next = Node(Node(1))
        assert node.is_leaf() is False
        # Attach right child node
        node.data.next = Node(Node(3))
        assert node.is_leaf() is False
        # Detach left child node
        node.next = None
        assert node.is_leaf() is False
        # Detach right child node
        node.data.next = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = Node(Node(2))
        assert node.is_branch() is False
        # Attach left child node
        node.next = Node(Node(1))
        assert node.is_branch() is True
        # Attach right child node
        node.data.next = Node(Node(3))
        assert node.is_branch() is True
        # Detach left child node
        node.next = None
        assert node.is_branch() is True
        # Detach right child node
        node.data.next = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = Node(Node(4))
        assert node.height_f() == 0
        # Attach left child node
        node.next = Node(Node(2))
        assert node.height_f() == 1
        # Attach right child node
        node.data.next = Node(Node(6))
        assert node.height_f() == 1
        # Attach left-left grandchild node
        node.next.next = Node(Node(1))
        assert node.height_f() == 2
        # Attach right-right grandchild node
        node.data.next.data.next = Node(Node(8))
        assert node.height_f() == 2
        # Attach right-right-left great-grandchild node
        node.data.next.data.next.next = Node(Node(7))
        assert node.height_f() == 3


class BinarySearchTreeTest(unittest.TestCase):

    def test_init(self):
        tree = BinarySearchTree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = BinarySearchTree([2, 1, 3])
        assert tree.root.data_f() == 2
        assert tree.root.left().data_f() == 1
        assert tree.root.right().data_f() == 3
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_strings(self):
        tree = BinarySearchTree(['B', 'A', 'C'])
        assert tree.root.data_f() == 'B'
        assert tree.root.left().data_f() == 'A'
        assert tree.root.right().data_f() == 'C'
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_tuples(self):
        tree = BinarySearchTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.root.data_f() == (2, 'B')
        assert tree.root.left().data_f() == (1, 'A')
        assert tree.root.right().data_f() == (3, 'C')
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_size(self):
        tree = BinarySearchTree()
        assert tree.size == 0
        tree.insert('B')
        assert tree.size == 1
        tree.insert('A')
        assert tree.size == 2
        tree.insert('C')
        assert tree.size == 3

    def test_search_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = BinarySearchTree(items)
        assert tree.search(1) == 1
        assert tree.search(2) == 2
        assert tree.search(3) == 3
        assert tree.search(4) is None

    def test_search_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search(8) is None

    def test_search_with_3_strings(self):
        # Create a complete binary search tree of 3 items in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        assert tree.search('A') == 'A'
        assert tree.search('B') == 'B'
        assert tree.search('C') == 'C'
        assert tree.search('D') is None

    def test_search_with_7_strings(self):
        # Create a complete binary search tree of 7 items in level-order
        items = ['D', 'B', 'F', 'A', 'C', 'E', 'G']
        tree = BinarySearchTree(items)
        for item in items:
            assert tree.search(item) == item
        assert tree.search('H') is None

    def test_insert_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        tree = BinarySearchTree()
        tree.insert(2)
        assert tree.root.data_f() == 2
        assert tree.root.left() is None
        assert tree.root.right() is None
        tree.insert(1)
        assert tree.root.data_f() == 2
        assert tree.root.left().data_f() == 1
        assert tree.root.right() is None
        tree.insert(3)
        assert tree.root.data_f() == 2
        assert tree.root.left().data_f() == 1
        assert tree.root.right().data_f() == 3

    def test_insert_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree()
        for item in items:
            tree.insert(item)
        assert tree.root.data_f() == 4
        assert tree.root.left().data_f() == 2
        assert tree.root.right().data_f() == 6
        assert tree.root.left().left().data_f() == 1
        assert tree.root.left().right().data_f() == 3
        assert tree.root.right().left().data_f() == 5
        assert tree.root.right().right().data_f() == 7

    def test_delete_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        items = [2, 1, 3]
        tree = BinarySearchTree(items)
        assert tree.root.data_f() == 2
        assert tree.root.left().data_f() == 1
        assert tree.root.right().data_f() == 3
        # TODO: Test structure of tree after each deletion
        tree.delete(2)
        assert tree.root.data_f() == 1
        assert tree.root.left() is None
        assert tree.root.right().data_f() == 3
        tree.delete(1)
        assert tree.root.data_f() == 3
        assert tree.root.left() is None
        assert tree.root.right() is None
        tree.delete(3)
        assert tree.root is None

    def test_delete_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # TODO: Test structure of tree after each deletion
        tree.delete(4)
        assert tree.root.data_f() == 3
        assert tree.root.left().data_f() == 2
        assert tree.root.right().data_f() == 6
        assert tree.root.right().right().data_f() == 7
        assert tree.root.right().left().data_f() == 5
        tree.delete(2)
        assert tree.root.data_f() == 3
        assert tree.root.left().data_f() == 1
        assert tree.root.right().data_f() == 6
        assert tree.root.right().right().data_f() == 7
        assert tree.root.right().left().data_f() == 5
        tree.delete(6)
        assert tree.root.data_f() == 3
        assert tree.root.left().data_f() == 1
        assert tree.root.right().data_f() == 5
        assert tree.root.right().right().data_f() == 7

    def test_items_in_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_pre_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == ['B', 'A', 'C']

    def test_items_post_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == ['A', 'C', 'B']

    def test_items_level_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]

    def test_items_pre_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the pre-order traversal of tree items is ordered correctly
        assert tree.items_pre_order() == [4, 2, 1, 3, 6, 5, 7]

    def test_items_post_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the post-order traversal of tree items is ordered correctly
        assert tree.items_post_order() == [1, 3, 2, 5, 7, 6, 4]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = BinarySearchTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]


if __name__ == '__main__':
    unittest.main()
