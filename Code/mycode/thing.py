def find_all_indexes(text, pattern, itext=0, ipattern=0, indices=[]):
    if len(text) == itext + ipattern:
        if len(pattern) == ipattern:
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
    return find_all_indexes(text, pattern, itext, ipattern, indices)


def test():
    print(f"the resul of 'abababa', 'aba': {find_all_indexes('abababa', 'aba')}")
    print(f"the resul of 'abababa', 'aba': {find_all_indexes('abababa', 'aba')}")
    print(f"the resul of 'abababa', 'aba': {find_all_indexes('abababa', 'aba')}")
test()
