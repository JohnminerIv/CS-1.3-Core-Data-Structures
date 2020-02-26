#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    """Same worst case as find_all_indexes()"""
    # TODO: Implement contains here (iteratively and/or recursively)
    # iterative or recursive
    array = find_all_indexes(text, pattern, 1)
    # array = find_all_indexes_r(text, pattern)
    if len(array) == 0:
        return False
    return True


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    """Same worst case as find_all_indexes()"""
    # TODO: Implement find_index here (iteratively and/or recursively)\
    # iterative or recursive
    array = find_all_indexes(text, pattern, 1)
    # array = find_all_indexes_r(text, pattern)
    if len(array) == 0:
        return None
    return array[0]


def find_all_indexes(text, pattern, callfrom=0):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    """ Time Complexity annotation!!!!
    t = len(text)
    p = len(pattern)
    worst_case_time_complexity = O(((t-p)*p)+(t-p)) or O(t*p)
    ((t-p)*p) is because each position might start a pattern and we check until the
    matching ends which might be the last letter of p. We won't check the places
    in the text if the pattern is to long to exist there.
    +(t-p) is because I didn't optimize."""
    lpattern = len(pattern)
    ltext = len(text)
    indexs = []
    for l in range(ltext):
        if lpattern == 0:
            indexs.append(l)
            if callfrom == 1:
                return indexs
        elif text[l] == pattern[0]:
            if lpattern + l <= ltext:
                for le in range(0, lpattern):
                    if text[l + le] != pattern[le]:
                        break
                    elif le == lpattern-1:
                        indexs.append(l)
                        if callfrom == 1:
                            return indexs
            else:
                break
        elif lpattern + l >= ltext:
            break
    return indexs


def find_all_indexes_r(text, pattern, itext=0, ipattern=0, indices=None):
    """Recursive implementation of find_all_indexes. The time complexity should
    be equialent to find all indexs not recursive."""
    if indices is None:
        indices = []
    if len(text) == itext + ipattern:
        if len(pattern) == ipattern and len(pattern) != 0:
            indices.append(itext)
        return indices
    elif len(pattern) == 0:
        indices.append(itext)
        itext += 1
    elif len(pattern) == ipattern:
        indices.append(itext)
        ipattern = 0
        itext += 1
    elif pattern[ipattern] == text[ipattern + itext]:
        ipattern += 1
    else:
        ipattern = 0
        itext += 1
    return find_all_indexes_r(text, pattern, itext, ipattern, indices)




def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
