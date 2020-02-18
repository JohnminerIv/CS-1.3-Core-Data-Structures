#!python

from strings import contains, find_index, find_all_indexes, find_all_indexes_r
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        # ...

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        # ...

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        # TODO: Write more positive test cases with assert equal int statements
        # ...

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        # ...

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_all_indexes_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indexes('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indexes('abc', 'a') == [0]  # single letters are easy
        assert find_all_indexes('abc', 'b') == [1]
        assert find_all_indexes('abc', 'c') == [2]
        assert find_all_indexes('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indexes('abc', 'bc') == [1]
        assert find_all_indexes('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indexes('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indexes('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indexes('abc', 'z') == []  # remember to test other letters
        assert find_all_indexes('abc', 'ac') == []  # important to test close cases
        assert find_all_indexes('abc', 'az') == []  # first letter, but not last
        assert find_all_indexes('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        # ...

    def test_find_all_indexes_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indexes('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indexes('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indexes('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indexes('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indexes('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indexes('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indexes('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indexes('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_my_own_cases(self):
        assert find_all_indexes('abababababababa', 'aba') == [0,2,4,6,8,10,12]
        assert find_all_indexes('levelevel', 'level') == [0,4]
        # worst case senario
        assert find_all_indexes('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah',
                                'aaaaaaaaaaah') == [32]
        assert find_all_indexes('ooooo', 'oo') == [0,1,2,3]
        assert find_all_indexes('topotopot', 'pot') == [2,6]
        assert find_all_indexes('tap', 'tap') == [0]

    def test_what_im_doing_with_my_life(self):
        assert find_all_indexes('\\', '\\') == [0]
        assert find_all_indexes('t\\\\', '\\') == [1,2]
        assert find_all_indexes('t\\\\', '\\\\') == [1]
        assert find_all_indexes('\n', '\n') == [0]
        assert find_all_indexes('\n\n', '\n') == [0,1]
        assert find_all_indexes('\ttap', 'tap') == [1]
        assert find_all_indexes('\ntap', 'tap') == [1]
        assert find_all_indexes('\ttap', '\ttap') == [0]
        assert find_all_indexes('\ntap', '\ntap') == [0]
        assert find_all_indexes('t\nap', 't\nap') == [0]
        assert find_all_indexes('\n', '') == [0]
        assert find_all_indexes('\ntap', '\ntap\n') == []
        assert find_all_indexes('\"\"\"hello\"\"\"', 'hello') == [3]

    def test_my_recursion(self):
        assert find_all_indexes_r('abababababababa', 'aba') == [0,2,4,6,8,10,12]
        assert find_all_indexes_r('levelevel', 'level') == [0,4]
        assert find_all_indexes_r('aaaaaaaaaaaaaaaaaaaaaaaah', 'aaaaaaaaaaah') == [13]
        assert find_all_indexes_r('ashhashash', 'hash') == [3,6]
        assert find_all_indexes_r('ooooo', 'oo') == [0,1,2,3]

    def test_my_recursion_non_matching(self):
        assert find_all_indexes_r('abababababababa', 'abc') == []
        assert find_all_indexes_r('abababababababa', 'aca') == []
        assert find_all_indexes_r('abababababababa', 'cba') == []
        assert find_all_indexes_r('cat', 'w') == []

    def test_my_recusionistic_stupidity(self):
        assert find_all_indexes_r('lol', '') == [0,1,2]
        assert find_all_indexes_r('lol', 'l') == [0,2]
        assert find_all_indexes_r('lol', 'lo') == [0]
        assert find_all_indexes_r('lol', 'ol') == [1]
        assert find_all_indexes_r('lol', 'lol') == [0]
        assert find_all_indexes_r('lol', 'lolo') == []
        assert find_all_indexes_r('', '') == []



if __name__ == '__main__':
    unittest.main()
