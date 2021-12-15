import unittest

import skin_siski


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getMult(), -20397256704000)


if __name__ == '__main__':
    unittest.main()
