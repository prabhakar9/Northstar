import unittest


def is_unique(s):
    char_map = [False for _ in range(128)]

    for i in range(len(s)):
        ord_ch = ord(s[i])

        if char_map[ord_ch]:
            return False
        else:
            char_map[ord_ch] = True
    return True


class Test(unittest.TestCase):
    dataT = [('abcde'), ('12arca'), ('s4fad'), ('')]
    dataF = [('hb 637jh=j ()'), ('23sd2')]

    def test_unique(self):
        test_string = ""
        try:
            for test_string in self.dataT:
                actual = is_unique(test_string)
                self.assertTrue(actual)

            for test_string in self.dataF:
                self.assertFalse(is_unique(test_string))
        except AssertionError:
            # print("Assertion failed with Input: {}".format(test_string))
            raise Exception("One or more unit tests failed - Input: {}".format(test_string))



if __name__ == "__main__":
    unittest.main()
