#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def create_base(base):
    chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    chars_array = [char for char in chars]
    if base <= 62:
        return chars_array[slice(base)]
    else:
        base -= 62
        indexs = [0]
        while base != 0:
            base -= 1
            reverse_indexs = [indexs[len(indexs)-i-1] for i in range(len(indexs))]
            combo_char = '('
            for index in reverse_indexs:
                combo_char += chars_array[index]
            combo_char += ')'
            chars_array.append(combo_char)
            indexs_full = 0
            for index in indexs:
                if index == 61:
                    indexs_full += 1
            if indexs_full == len(indexs):
                indexs = [0 for index in range(indexs_full + 1)]
            for index in range(len(indexs)):
                if indexs[index] == 61:
                    if index != len(indexs) - 1:
                        indexs[index] = 0
                        indexs[index + 1] += 1
            indexs[0] += 1
    return chars_array


def r_split(digits, base1, base2):
    pass


def r_encode(digits, base):
    pass


def r_decode(digits, base):
    pass


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    # assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    base_chars_array = create_base(base)
    len_of_number = len(digits) - 1
    deci_number = 0
    for place in digits:
        deci_number += base_chars_array.index(place) * (base ** len_of_number)
        len_of_number -= 1
    return deci_number
    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    # assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    # assert number >= 0, 'number is negative: {}'.format(number)
    base_chars_array = create_base(base)
    exponent = 0
    en_number = []
    while number - (base**exponent) > 0:
        exponent += 1
    for i in range(exponent+1):
        i = exponent - i
        en_number.append(base_chars_array[number // (base**i)])
        number = number - (number // (base**i))*(base**i)
    not_zero = lambda num: ((num != 0 and en_number[num] != '0') or (num == 0 and en_number[0] != '0') or num > 0 or len(en_number) == 1)
    return ''.join([en_number[num] for num in range(len(en_number)) if not_zero(num)])
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    # assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    # assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    return encode(decode(digits, base1), base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(encode(1009, 50))
    # print(decode('1001', 3))
    # print(create_base(500))
