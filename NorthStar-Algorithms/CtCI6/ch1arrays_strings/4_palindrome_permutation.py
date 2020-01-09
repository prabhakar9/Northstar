import unittest
from collections import Counter


def check_palindrome_permutation(s):
    counter = Counter()
    count = 0

    for c in s:
        if c != " ":
            if counter[c.lower()] == 0:
                count += 1
                counter[c.lower()] += 1
            else:
                count -= 1
                counter[c.lower()] -= 1

    if count <= 1:
        return True
    else:
        return False


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_palindrome_permutation(self):
        for test_string, result in self.data:
            actual = check_palindrome_permutation(test_string)
            self.assertEqual(actual, result)


if __name__ == "__main__":
    unittest.main()
