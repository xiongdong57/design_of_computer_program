# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    def is_palidrome(text):
        if len(text) >= 2:
            text = text[0].lower() + text[1:-1] + text[-1].lower()
        return text[::-1] == text
    maxlen = 0
    length = len(text)
    if length > 1:
        for i in range(length):
            for j in range(i, length + 1):
                sub_text = text[i:j]
                if is_palidrome(sub_text) and len(sub_text) >= maxlen:
                    maxlen = len(sub_text)
                    loc = (i, j)
        return loc
    else:
        return (0, 0)


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())
