import unittest

import skin_siski


class MyTestCase(unittest.TestCase):
    def test_valid(self):
        skin_siski.readNums("./validTest.txt")
        self.assertEqual(len(skin_siski.numbers), 6)


if __name__ == '__main__':
    unittest.main()
