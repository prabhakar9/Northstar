import unittest


def urlify(s, l):
    new_index = len(s)

    for i in reversed(range(l)):
        if s[i] == ' ':
            s[new_index-3:new_index] = '%20'
            new_index -= 3
        else:
            s[new_index-1] = s[i]
            new_index -= 1
    return s


class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for test_string, length, result in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, result)


if __name__ == "__main__":
    unittest.main()
