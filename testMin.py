import unittest

import skin_siski


class MyTestCase(unittest.TestCase):

    def test_min(self):
        skin_siski.readNums("./simpleTest.txt")
        self.assertEqual(skin_siski.getMin(), -5)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
