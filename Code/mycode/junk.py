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