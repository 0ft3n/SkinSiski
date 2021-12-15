import unittest

import skin_siski


class MyTestCase(unittest.TestCase):
    def test_max(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getMax(), 324)


if __name__ == '__main__':
    unittest.main()
