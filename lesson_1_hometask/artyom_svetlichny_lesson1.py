# Задание №1:
# Создать 5 переменных , две типа int , две типа str и
# одну типа list, list должен содержать минимум 5 значений.

print(f'Задание №1')
first_int_variable = 23
print('first_int_variable =', first_int_variable)
second_int_variable = 9
print('second_int_variable =', second_int_variable)
first_str_variable = 'first'
print('first_str_variable =', first_str_variable)
second_str_variable = 'second'
print('second_str_variable =', second_str_variable)
first_list = [1, 34, 'hello', 'world', 54]
print('first_list =', first_list)

# Задание №2:
# объявить новую переменную типа int и присвоить ей результат
# операции сложения первых двух переменных.
# Сделать тоже самое для остальных операций , возведение в степень,
# нахождение остатка, умножение, деление и деление без остатка

print(f'Задание №2')
third_int_variable = first_int_variable + second_int_variable
print('third_int_variable =', third_int_variable)
third_int_variable = first_int_variable ** second_int_variable
print('exponentiation =', third_int_variable)
third_int_variable = first_int_variable * second_int_variable
print('multiplication =', third_int_variable)
third_int_variable = first_int_variable / second_int_variable
print('division =', third_int_variable)
third_int_variable = first_int_variable // second_int_variable
print('division without remainder =', third_int_variable)

# Задание №3:
# объявить новую переменную и инициализировать ее значением
# списка созданного в первом задании , но с использованием среза
# с 1-ого индекса по 4-ый (инициализация - просто присвоение значения,
# типа age = 29)

print(f'Задание №3')
second_list = first_list[1:4]
print('second_list =', second_list)

# Задание №4:
# инциализировать новую переменную результатом сложения (конкатинации)
# двух переменных типа str созданных на первом этапе так , чтобы
# при вызове функции print() с этой переменной вывод происходил с пробелом
# между ними. Пример name = 'Valerij' last_name = 'Zhuk'
# print(full_name) >>> 'Valerij Zhuk'

print(f'Задание №4')
fourth_str_variable = first_str_variable + ' ' + second_str_variable
print('fourth_str_variable =', fourth_str_variable)

# Задание #5:
# Инициализировать переменную
# just_dict = {"name": "это замените вашим именем", age: 20}
# поменять значение переменной just_dict по ключу name
# и присвоить туда любое новое имя
# После чего создать переменную age и записать в нее значение
# ключа age из just_dict

print(f'Задание №5')
just_dict = {'name': 'Alex', 'age': 20}
print('just_dict =', just_dict)
just_dict['name'] = "Artyom"
print('just_dict =', just_dict)
age = just_dict['age']
print('age =', age)
