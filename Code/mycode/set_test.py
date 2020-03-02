import unittest
from set import Setree

class SetTest(unittest.TestCase):
    def set_add_edges(self):
        set = Setree()
        set.add(5)
        set.add(5)
        assert set.in_order() == [5]
        set.add(4)
        set.add(6)
        set.add(5)
        assert set.in_order() == [4, 5, 6]
        set.remove(5)
        assert set.in_order() == [4, 6]
        set.add(5)
        assert set.in_order() == [4, 5, 6]
        set = Setree([5,5,5])
        assert set.in_order() == [5]

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
        assert set.contains(6) == False
        assert set.contains(78) == False

    def test_set_delete(self):
        set = Setree([8,7,9,4,5,23,15,87])
        assert set.size == 8
        assert set.in_order() == [4,5,7,8,9,15,23,87]
        set.remove(8)
        assert set.size == 7
        assert set.in_order() == [4,5,7,9,15,23,87]
        set.remove(87)
        assert set.size == 6
        assert set.in_order() == [4,5,7,9,15,23]
        set.remove(15)
        assert set.size == 5
        assert set.in_order() == [4,5,7,9,23]
        set.remove(7)
        assert set.size == 4
        assert set.in_order() == [4,5,9,23]
        set.remove(9)
        assert set.size == 3
        assert set.in_order() == [4,5,23]
        set.remove(4)
        assert set.size == 2
        assert set.in_order() == [5,23]
        set.remove(5)
        assert set.size == 1
        assert set.in_order() == [23]
        set.remove(23)
        assert set.size == 0
        assert set.in_order() == []

    def test_set_intersection(self):

        set1 = Setree([8,7,9,4,5,23,15,87])
        set2 = Setree([23,15,87,100,9000])
        set3 = Setree([40,15,100,9])
        intersection = set1.intersection(set2)
        assert intersection.in_order() == [15, 23, 87]
        intersection = set2.intersection(set1)
        assert intersection.in_order() == [15, 23, 87]
        intersection = set1.intersection(set3)
        assert intersection.in_order() == [9, 15]
        intersection = set3.intersection(set1)
        assert intersection.in_order() == [9, 15]
        intersection = set2.intersection(set3)
        assert intersection.in_order() == [15, 100]
        intersection = set3.intersection(set2)
        assert intersection.in_order() == [15, 100]
        intersection = set1.intersection(set2.intersection(set3))
        assert intersection.in_order() == [15]


    def test_set_union(self):
        set1 = Setree([8,7,9,4,5,23,15,87])
        set2 = Setree([1,23,15,87,65,2,3,100,9000])
        set3 = Setree([-1,-2,-3,9,65])
        union = set1.union(set2)
        assert union.in_order() == [1,2,3,4,5,7,8,9,15,23,65,87,100,9000]
        union = set2.union(set1)
        assert union.in_order() == [1,2,3,4,5,7,8,9,15,23,65,87,100,9000]
        union = set1.union(set3)
        assert union.in_order() == [-3,-2,-1,4,5,7,8,9,15,23,65,87]
        union = set3.union(set1)
        assert union.in_order() == [-3,-2,-1,4,5,7,8,9,15,23,65,87]
        union = set2.union(set3)
        assert union.in_order() == [-3,-2,-1,1,2,3,9,15,23,65,87,100,9000]
        union = set3.union(set2)
        assert union.in_order() == [-3,-2,-1,1,2,3,9,15,23,65,87,100,9000]
        union = set1.union(set2.union(set3))
        assert union.in_order() == [-3,-2,-1,1,2,3,4,5,7,8,9,15,23,65,87,100,9000]

    def test_set_is_subset(self):
        set1 = Setree([8,7,9,4,5,23,15,87])
        set2 = Setree([23,15,87,100,9000])
        set3 = Setree([23,15,87])
        set4 = Setree([23,15,87])
        assert set1.is_subset(set2) is False
        assert set2.is_subset(set1) is False
        assert set1.is_subset(set3) is True
        assert set3.is_subset(set1) is False
        assert set2.is_subset(set3) is True
        assert set3.is_subset(set2) is False
        assert set3.is_subset(set4) is True
        assert set4.is_subset(set3) is True


if __name__ == '__main__':
    unittest.main()
