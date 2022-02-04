# Task 1
lst = [1, 2, 3, 4, 5]
print('Task 1, way 1: ', sum(lst))

lst_sum = 0
for num in lst:
    lst_sum += num
print('Task 1, way 2: ', lst_sum)
print()

# Task 2
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_sum = 0
for num in lst:
    if num % 2 == 0:
        lst_sum += num
print('Task 2, way 1: ', lst_sum)

print('Task 2, way 2: ', sum(num for num in lst if num % 2 == 0))
print()

# Task 3
mix_tuple = (1, 2, 3, 8.2, 34, 22.54)
print('Task 3: ', end='')
print(*(num for num in mix_tuple if isinstance(num, int)), sep=', ')
print()

# Task 4
tup = (1, 23, 321, 67, 8, 0)
print('Task 4:')
for num in enumerate(tup, 1):
    print(*num, sep=': ')
print()

# Task 5
dictionary = {'alpha': 1, 'beta': 2, 'gamma': 3}

print('Task 5, Way 1: ', end='')
for key in dictionary:
    print(key, end=' ')
print()

print('Task 5, Way 2:', *dictionary)
print()

# Task 6
dictionary = {'alpha': 1, 'beta': 2, 'gamma': 3}
print('Task 6:')
for key, value in dictionary.items():
    print(key, '-', value)
print()

# Task 7
fruit_dict = {'banana': 10, 'apple': 5, 'pomelo': 15}
fruit_lst = ['orange', 'banana', 'pear', 'apple', 'pomelo', 'pineapple']
print('Task 7:')
for fruit in fruit_lst:
    if fruit in fruit_dict:
        print(fruit + ' - ' + str(fruit_dict[fruit]))
print()

# Task 8
lst = ['Denis', 'Alex', 'Ivan']

new_lst = []
print('Task 8, Way 1:', end=' ')
for name in lst:
    new_lst.append('Dr. ' + name)
print(*new_lst, sep=', ')

new_lst = ['Dr. ' + name for name in lst]
print('Task 8, Way 2:', end=' ')
print(*new_lst, sep=', ')
print()

# Task 9
lst_div_eight = [num for num in range(1, 1001) if num % 8 == 0]

# Task 10
lst = [1, 15, 100, 46, 45, 100, 89, 89, 100]
count = 0
print('Task 10:')
while count < len(lst):
    if lst[count] == 100:
        print(f'There is a 100 at index no: {str(count)}')
    count += 1