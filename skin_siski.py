numbers = []


def readNums(file):
    numbers.clear()
    with open(file) as text:
        for line in text.readlines():
            for number in line.split(" "):
                if number.isdigit() or (number.startswith("-") and number[1:].isdigit()):
                    numbers.append(int(number))


def getSum():
    result = 0
    for number in numbers:
        result += number
    return result


def getMin():
    m = 0
    for i in range(len(numbers)):
        if i == 0 or numbers[i] < m:
            m = numbers[i]
    return m


def getMax():
    m = 0
    for i in range(len(numbers)):
        if i == 0 or numbers[i] > m:
            m = numbers[i]
    return m


def getMult():
    result = 1
    for number in numbers:
        try:
            result *= number
        except OverflowError:
            print("Слишком большое значение произведения! Возвращаем то, что смогли насчитать :)")
            break
    return result


#readNums("test/100.txt")
#print(f"Минимум {getMin()}")
#print(f"Максимум {getMax()}")
#print(f"Сумма {getSum()}")
#print(f"Произведение {getMult()}")
