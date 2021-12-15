import unittest
import skin_siski
import time


class MyTestCase(unittest.TestCase):

    def test_valid(self):
        skin_siski.readNums("validTest.txt")
        self.assertEqual(len(skin_siski.numbers), 4)

    def test_min(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getMin(), -5)

    def test_max(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getMax(), 324)

    def test_sum(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getSum(), 449)

    def test_multiply(self):
        skin_siski.readNums("simpleTest.txt")
        self.assertEqual(skin_siski.getMult(), -20397256704000)

    def test_1(self):
        print("Проверка времени выполнения с файлом 1KB")
        start_time = time.time()
        skin_siski.readNums("simpleTest.txt")
        print(f"Время чтения чисел из файла: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMin()
        print(f"Время поиска минимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMax()
        print(f"Время поиска максимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getSum()
        print(f"Время вычисления суммы: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMult()
        print(f"Время вычисления произведения: {time.time() - start_time} секунд")
        print()
        self.assertTrue(True, "sd")

    def test_100(self):
        print("Проверка времени выполнения с файлом 100KB")
        start_time = time.time()
        skin_siski.readNums("100.txt")
        print(f"Время чтения чисел из файла: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMin()
        print(f"Время поиска минимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMax()
        print(f"Время поиска максимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getSum()
        print(f"Время вычисления суммы: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMult()
        print(f"Время вычисления произведения: {time.time() - start_time} секунд")
        print()
        self.assertTrue(True)

    def test_500(self):
        print("Проверка времени выполнения с файлом 500KB")
        start_time = time.time()
        skin_siski.readNums("500.txt")
        print(f"Время чтения чисел из файла: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMin()
        print(f"Время поиска минимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMax()
        print(f"Время поиска максимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getSum()
        print(f"Время вычисления суммы: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMult()
        print(f"Время вычисления произведения: {time.time() - start_time} секунд")
        print()
        self.assertTrue(True)

    def test_1000(self):
        print("Проверка времени выполнения с файлом 1MB")
        start_time = time.time()
        skin_siski.readNums("1000.txt")
        print(f"Время чтения чисел из файла: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMin()
        print(f"Время поиска минимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMax()
        print(f"Время поиска максимума: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getSum()
        print(f"Время вычисления суммы: {time.time() - start_time} секунд")
        start_time = time.time()
        skin_siski.getMult()
        print(f"Время вычисления произведения: {time.time() - start_time} секунд")
        print()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
