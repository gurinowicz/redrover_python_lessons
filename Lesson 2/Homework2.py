# Задание 2.1
# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
#
# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
#
# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
#
# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()
#
# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}


# HOMEWORK Задание 2.1
health = int(input('Введите цифры: '))

if health >= 0:
    print(f'{health} - Ты можешь продолжать')
else:
    print(f'{health} - Недостаточно здоровья для продолжения игры')

# HOMEWORK Задание 2.2
a = int(input('Enter a number: '))
if a%2 == 0:
    print(a, "It's an odd number")

else:
    print(a, "It's an even number")

# Задание 2.3

a = int(input('Enter a year: '))
if a%4 == 0:
    if a/400 == 0:
        if a%100 ==0:
            print(a, "високосный")
        else:
            print(a, "Невисокосный")
    else: print(a, "високосный")
else:
    print(a, "Всё равно Невисокосный")

# Задание 2.4
text = str(input('Enter any text: '))
num = int(input('Enter quantity of repetition text: '))
i = 1
while i <= num:
    print(text)
    i += 1

# HOMEWORK Задание 2.5
a = int(input('Enter a first number: '))
c = int(input('Enter a second number: '))
b = str(input('Enter an operator: '))
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a * c)
elif b == '/':
    print(abs(a/c))
