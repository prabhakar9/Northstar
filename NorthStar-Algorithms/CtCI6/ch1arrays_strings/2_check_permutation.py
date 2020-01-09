import unittest
from collections import Counter


def check_permutation(s1, s2):
    counter = Counter()

    if len(s1) != len(s2):
        return False

    for c in s1:
        counter[c] += 1

    for c in s2:
        if counter[c] == 0:
            return False
        else:
            counter[c] -= 1

    return True


class Test(unittest.TestCase):
    dataT = [('abcde', 'deabc'), ('12afbt34', 'aftb3421'), ('wef34f', 'wffe34')]
    dataF = [('abcde', 'dbc2a'), ('2354', '1234'), ('efsd', 'ef3sd'), ('dcw4f', 'dcw5f')]

    def test_check_permutation(self):
        for test_strings in self.dataT:
            # print(*test_strings)
            result = check_permutation(*test_strings)
            self.assertTrue(result)

        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
