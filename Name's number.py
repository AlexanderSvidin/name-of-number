import math

# Вводим натуральное число
number = int(input("Введите число: "))

# Функция контроля ввода: проверяет число на положительность
def conrol_input_num(number):
    while number <= 0:
        print("\nОшибка! Введите положительное число: ", end="")
        number = int(input())

    return number

# Контроль ввода: проверка числа на натуральность
conrol_input_num(number)

# Определим кол-во классов в числе
def count_classes(number):
    return math.ceil(len(str(number)) / 3)
    
print("\nКол-во классов:", count_classes(number))

# Функция возвращающая перевёрнутое значение
def reverse_num(number):
    reverse_number = ""
    for symbol in str(number):
        reverse_number = symbol + reverse_number
    return reverse_number # Возвращает строковый тип данных

# Функция возвращающая корректный вид числа(есть отступы)
def correct_number(number):
    
    number = reverse_num(number)
    correct_num = ""
    count = 0
    for symbol in number:
        
        count += 1
        correct_num += symbol
        
        if count == 3:
            correct_num += " "
            count = 0

    correct_num = reverse_num(correct_num)
    return correct_num # Возвращает строковый тип данных

print("Корректный вид числа:", correct_number(number))

# Правильное название числа
text = ""
for clas in range(count_classes(number)):
    for digit in  