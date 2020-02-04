#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    lpattern = len(pattern)
    ltext = len(text)
    for l in range(ltext):
        if lpattern == 0:
            return True
        if text[l] == pattern[0]:
            count = 1
            if lpattern + l <= ltext:
                for le in range(1, lpattern):
                    if text[l + le] == pattern[le]:
                        count += 1
                    else:
                        break
            if count == lpattern:
                return True
    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    lpattern = len(pattern)
    ltext = len(text)
    index = None
    for l in range(ltext):
        if lpattern == 0
            return l
        if text[l] == pattern[0]:
            count = 1
            if lpattern + l <= ltext:
                for le in range(1, lpattern):
                    if text[l + le] == pattern[le]:
                        count += 1
                    else:
                        break
            if count == lpattern:
                return l
    return index


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    lpattern = len(pattern)
    ltext = len(text)
    indexs = []
    for l in range(ltext):
        if lpattern == 0:
            indexs.append(l)
        elif text[l] == pattern[0]:
            if lpattern + l <= ltext:
                for le in range(0, lpattern):
                    if text[l + le] != pattern[le]:
                        break
                    elif le == lpattern-1:
                        indexs.append(l)
            else:
                break
        elif lpattern + l >= ltext:
            break
    return indexs


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
