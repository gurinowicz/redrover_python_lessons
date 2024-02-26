# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
my_list = ['a', 'b', [1, 2, 3], 'd']
print('Result of HW#3.1: ', *my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
lst2 = sum(summ for summ in list_1 if isinstance(summ, int))
print("HW#3.2 Sum of all the elements in the list is:", lst2, "And all words with 'A': ", [x for x in list_1 if type(x)==str and 'a' in x])


# 3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

lst3 = ['cat', 'dog', 'horse', 'cow']
print("HW#3.3: ", tuple(lst3))
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input('Enter members of 1st family: ').split(',')
family_2 = input('Enter members of 2nd family: ').split(',')
if len(family_1) == len(family_2):
    print("HW#3.3:  , Equal")
elif len(family_1) > len(family_2):
    print(f'Family_1 is bigger')
else:
    print(f'Family_2 is bigger')
#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
my_dict = {
    "title": "Lords of the Rings",
    "director": "Peter Jackson",
    "year": 	2001,
    "budget": "$281 million",
    "main_actor": "Elijah Wood",
    "slogan": "The Fellowship of the Ring"
}
print(my_dict.values())
print(my_dict.keys())

for key, value in my_dict.items():
    print(f'{key}:{value}')

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
sum3 = my_dictionary.values()
print(sum(sum3))
# opt2
sum0 = 0
for summa in my_dictionary.values():
    sum0 = summa+sum0
print("HW#3.6: ", sum0)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
lst3 = [1, 2, 3, 4, 5, 3, 2, 1]
set_list = set(lst3)
print("HW#3.7: ", set_list)
#
# # opt2
lst4 = []
for i in lst3:
    if i not in lst4:
        lst4.append(i)
print("HW#3.7: ", lst4)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print("HW#3.8, значения, которые встречаются в обоих множествах: ",set2.intersection(set1))
print("HW#3.8, значения, которые не встречаются в обоих множествах: ", set2.difference(set1))
print("HW#3.8,являются ли эти множества подмножествами друг друга: ", set1 in set2)