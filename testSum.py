import unittest

import skin_siski


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getSum(), 449)


if __name__ == '__main__':
    unittest.main()
