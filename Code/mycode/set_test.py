import unittest
from set import Setree

class SetTest(unittest.TestCase):
    def test_set_contains(self):
        set = Setree([8,7,9,4,5,23,15,87])
        assert set.contains(8) == True
        assert set.contains(7) == True
        assert set.contains(9) == True
        assert set.contains(4) == True
        assert set.contains(5) == True
        assert set.contains(23) == True
        assert set.contains(15) == True
        assert set.contains(87) == True
        assert set.contains(0) == False

    def test_set_delete(self):
        set = Setree([8,7,9,4,5,23,15,87])
        assert set.size() == 8
        assert set.in_order() == [4,5,7,8,9,15,23,87]
        set.remove(8)
        assert set.size() == 7
        assert set.in_order() == [4,5,7,9,15,23,87]
        set.remove(87)
        assert set.size() == 6
        assert set.in_order() == [4,5,7,9,15,23]
        set.remove(15)
        assert set.size() == 5
        assert set.in_order() == [4,5,7,9,23]
        set.remove(7)
        assert set.size() == 4
        assert set.in_order() == [4,5,9,23]
        set.remove(9)
        assert set.size() == 3
        assert set.in_order() == [4,5,23]
        set.remove(4)
        assert set.size() == 2
        assert set.in_order() == [5,23]
        set.remove(5)
        assert set.size() == 1
        assert set.in_order() == [23]
        set.remove(23)
        assert set.size() == 0
        assert set.in_order() == []

    def test_set_intersection(self):
        set = Setree([8,7,9,4,5,23,15,87])
        nset = Setree([23,15,87,100,9000])
        nnset = set.intersection(nset)
        assert nnset.in_order() == [15, 23, 87]

    def test_set_union(self):
        set = Setree([8,7,9,4,5,23,15,87])
        nset = Setree([1,23,15,87,65,2,3,100,9000])
        nnset = set.union(nset)
        assert nnset.in_order() == [1,2,3,4,5,7,8,9,15,23,65,87,100,9000]

    def test_set_is_subset(self):
        set = Setree([8,7,9,4,5,23,15,87])
        nset = Setree([23,15,87,100,9000])
        assert set.is_subset(nset) is False
        nset = Setree([23,15,87])
        assert set.is_subset(nset) is True
