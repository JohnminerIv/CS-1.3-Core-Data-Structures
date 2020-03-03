def stupidity(new_item, ls=[]):
    ls.append(new_item)
    return ls


def test_stupidity():
    assert stupidity(1) == [1]
    assert stupidity(1, [2]) == [2, 1]
    assert stupidity(2) == [1, 2]
    assert stupidity(3) == [1, 2, 3]
    assert stupidity(4, []) == [4]
