# Task 1
# Создать 5 переменных , две типа int , две типа str и одну типа list, list должен содержать минимум 5 значений.
first_int = 17
second_int = 25
first_str = 'Python'
second_str = 'World'
first_list = [17, 5, 19, 88, 33]

print(first_int, second_int, first_str, second_str, first_list)

# Task 2
# объявить новую переменную типа int и присвоить ей результат операции сложения первых двух переменных.
# Сделать тоже самое для остальных операций, возведение в степень,
# нахождение остатка, умножение, деление и деление без остатка.

int_sum = first_int + second_int
degree = first_int ** 2
modulo = second_int % 3
mult = first_int * second_int
div = second_int / 5
div_2 = second_int // first_int

# Task 3
# объявить новую переменную и инициализировать ее значением
# списка созданного в первом задании , но с использованием среза
# с 1-ого индекса по 4-ый (инициализация - просто присвоение значения, типа age = 29)

second_list = first_list[0:3]

# Task 4
# инциализировать новую переменную результатом сложения (конкатинации)
# двух переменных типа str созданных на первом этапе так , чтобы
# при вызове функции print() с этой переменной вывод происходил с пробелом
# между ними. Пример name = 'Valerij' last_name = 'Zhuk'
# print(full_name) >>> 'Valerij Zhuk'

full_str = first_str + ' ' + second_str
print(full_str)

# Task 5
# Инициализировать переменную just_dict = {"name": "это замените вашим именем", age: 20}
# поменять значение переменной just_dict по ключу name
# и присвоить туда любое новое имя После чего создать переменную age и записать в нее значение ключа age из just_dict

just_dict = {'name': 'Valerij Zhuk', 'age': 33}
just_dict['name'] = 'Valera'
age = just_dict['age']