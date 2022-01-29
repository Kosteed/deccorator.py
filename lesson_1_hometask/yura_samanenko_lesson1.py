#Задание 1
a = 5
print('a',a )
b = 2
print('b',b )
name = 'yura'
print('neme', name )
surname = 'samanenko'
print('surname',surname )
spisok = ['с','п','и','с','о','к',]

#Задание 2
summa = a + b
print('Сложение',summa )
rate = a ** b
print('возведение в степень',rate )
multiplication = a * b
print('умножение',multiplication )
division = a / b
print('деление',division )
find = a % b
print('остаток',find )
c = a // b
print('деление без остатка', c )

#Задание 3
srez = spisok [1:4]
print(' срез ', srez )

#Задание 4
fullname = name + ' ' + surname
print(' Полное имя ', fullname)

#Задание 5
just_dict = {"name": "Yura", "age": 29}
print('Имя и возраст ', just_dict)
just_dict["name"] = "yuri"
print('Имя и возраст ', just_dict)
age = just_dict['age']
print(' Возраст по ключу', age)