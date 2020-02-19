        # print(f'1 n {number} b {base} p {power} the_num {the_number}')
        if number - (base ** power) == 0:
            # print('if')
            the_number += base_chars_array[1]
            for placeholder in range(power):
                the_number += '0'
            number = 0


                        if number - (index1*(base**power)) < 0 and number - (index2*(base**power)) > 0:
                            # print('First')
                            the_number += base_chars_array[index1]
                            number -= ((index1-1)*(base**power))
                            found_correct = True


    index1 = 0
    index2 = base
    while number != 0:
        if number - (base ** power) > 0:
            # print(f'elif n {number} b {base} p {power} ')
            power += 1
        else:
            # print('else')
            power -= 1
            while power >= 0:
                found_correct = False
                index1 = 0
                index2 = base
                if number - (base**power) < 0:
                    the_number += '0'
                else:
                    while found_correct is False:
                        # print(f'2 n {number} b {base} p {power} the_num {the_number}')
                        index1 += 1
                        index2 -= 1
                        if number - (index1*(base**power)) < 0:
                            # print('Second')
                            the_number += base_chars_array[index1-1]
                            number -= ((index1-1)*(base**power))
                            found_correct = True
                        elif number - (index2*(base**power)) >= 0:
                            # print('Third', number - ((index2*base)**power))
                            the_number += base_chars_array[index2]
                            number -= ((index2)*(base**power))
                            found_correct = True
                power -= 1
    return the_number


    search = 0
    index = 0
    len_array = len(array) - 1
    sqrt_len = math.sqrt(len_array)
    print(sqrt_len)
    while array[index] != item and search < math.floor(sqrt_len):
        index += ((len_array-index)//2)
        print((index, search))
        if (item == array[index]) is True:
            return index - 1
        if (item > array[index]) is True:
            print('1')
            index += 1
        else:
            print('2')
            len_array = index - 1
        search += 1
    return None


def solution(string,markers):
    #your code here
    len_str = len(string)
    after = False
    new_string = ''
    for i in range(len_str):
        if after is True and i + 1 != len_str:
            print('hi')
            if string[i] + string[i+1] == '\\\n':
                after = False
                new_string += string[i]
        if string[i] in markers or after is True:
            after = True
        else:
            new_string += string[i]
    return new_string




    if len(pattern) == 0:
        # print(len(pattern) == 0)
        # print(pattern)
        if len(indices) == len(text):
            return indices
        indices.append(itext)
    elif len(pattern) == ipattern:
        print(len(pattern) == ipattern)
        print(pattern)
        itext -= ipattern
        indices.append(itext)
        ipattern = 0
    elif len(text) == itext:
        return indices
    elif pattern[ipattern] == text[itext]:
        ipattern += 1
    else:
        ipattern = 0
    itext += 1
    return find_all_indexes(text, pattern, itext, ipattern, indices)
