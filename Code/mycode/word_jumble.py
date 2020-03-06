import sys


def gernerate_anagrams_soreted_dict(file='/usr/share/dict/words'):
    dict = {}
    with open(file) as file:
        for line in file:
            line = line.strip()
            key = ''.join(sorted(line))
            srts_list = dict.get(key)
            if srts_list is None:
                srts_list = []
            srts_list.append(line)
            dict[key] = srts_list
    return dict


def find_anagrams(ls):
    dict = gernerate_anagrams_soreted_dict()
    list_of_words = []
    for word in ls:
        word = word.strip()
        key = ''.join(sorted(word.strip()))
        ls2 = dict.get(key)
        if ls2 is None:
            ls2 = None
        list_of_words.append((word, ls2))
    return list_of_words


def permutaions_r(letters):
    if len(letters) == 1:
        return letters
    perm = []
    for letter in range(len(letters)):
        remaining_elements = ''.join([letters[nletter] for nletter in range(len(letters)) if nletter != letter])
        possible = permutaions_r(remaining_elements)
        for possibilities in possible:
            perm.append(letters[letter] + possibilities)
    return perm


def permutations_r_ls(words_p):
    if len(words_p) == 1:
        return words_p[0]
    perm = []
    for word in range(len(words_p)):
        remaining_elements = ''.join([words_p[word] for word in range(len(words_p)) if word != word])
        possible = permutations_r_ls(remaining_elements)
        for possibilities in possible:
            for possible_word_1 in possibilities:
                for possible_word_2 in word:
                    perms_of_this_combination = permutaions_r(possible_word_1 + possible_word_2)
                    perm.append(perms_of_this_combination)
    return perm


def find_circle_values(words_ls_ls, circles):
    combinations = []
    for word_ls in range(len(words_ls_ls)):
        possible_words = []
        for word in words_ls_ls[word_ls]:
            possible_letters = ''
            for letter in range(len(word)):
                if circles[word_ls][letter] == 'O':
                    possible_letters += word[letter]
            possible_words.append(possible_letters)
        combinations.append(possible_words)
    return combinations




def main(args, circles=None, final=None):
    if circles is None:
        print(find_anagrams(args))
    else:
        """
        valid_anagrams = find_anagrams(args)
        possible_permutations =
        """
        pass


if __name__ == '__main__':
    """
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print(find_anagrams(['sett', 'hits', 'scae', 'leapse']))
    """
    # print(permutaions_r('1234567890'))
    print(permutations_r_ls(find_circle_values([['hello', 'baele']], ['_O__O'])))
