#task 1

number_1 = 5
number_2 = 2

name_1 = 'Denis'
name_2 = 'Biryukov'

arr = [1, 2, 3, 4, 5, 'xyz', [1, 2]]

#task 2

number_summ = number_1 + number_2
number_sqr = number_1 ** number_2
number_resid = number_1 % number_2
number_mult = number_1 * number_2
number_div = number_1 / number_2
number_div2 = number_1 // number_2

print('summ: ' + str(number_summ), 'sqr: ' + str(number_sqr),
      'resid: ' + str(number_resid), 'mult: ' + str(number_mult),
      'div: ' + str(number_div), 'div2: ' + str(number_div2), sep='\n')

#task 3

arr_2 = arr[1:4]
print(arr_2)

#task 4

name_3 = name_1 + ' ' + name_2
print(name_3)

#task 5

just_dict = {'name': 'Denis', 'age': 23}
print(just_dict)
just_dict['name'] = 'Alex'
print(just_dict)

age = just_dict['age']