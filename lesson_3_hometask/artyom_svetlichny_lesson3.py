# Task №1

list_of_numbers = [1, 23, 2, 67, 54, 14, 35]
sum_of_numbers = 0

for num in list_of_numbers:
    sum_of_numbers += num

print(f"Sum of all numbers in a list = {sum_of_numbers}")

# Task №2

list_of_numbers = [1, 23, 2, 67, 54, 14, 35]
sum_of_even_numbers = 0

for num in list_of_numbers:
    if num % 2 == 0:
        sum_of_even_numbers += num

print(f"Sum of all even numbers in a list = {sum_of_even_numbers}")

# Task №3

mix_data_tuple = ("Winter", 12.43, 23, 32.32, 98, "Phone")
tuple_of_integers = ()
for item in mix_data_tuple:
    if isinstance(item, int):
        tuple_of_integers += (item,)

print(tuple_of_integers)

# Task №4

# Variant 1

for item in enumerate(mix_data_tuple):
    print(item)

# Variant 2

for index, item in enumerate(mix_data_tuple):
    print(index, item)

# Task №5

car_dict = {"brand": "Tesla", "model": "Model S Plaid", "year": 2021}

print(car_dict.keys())

for keys in car_dict.keys():
    print(keys)

# Task №6

for keys, values in car_dict.items():
    print(keys, values)

# Task №7

fruits_dict = {"apples": 23, "oranges": 12, "bananas": 9, "lemons": 4, "mango": 2}
fruits_list = ["apples", "oranges", "bananas"]

for item in fruits_list:
    if item in fruits_dict:
        print(item, fruits_dict.get(item))

# Task №8

list_of_names = ["German", "Alex", "Kseniya", "Stanislav", "Kirill"]
list_of_doctors_names = []

for item in list_of_names:
    list_of_doctors_names.append(f"Dr.{item}")

print(list_of_doctors_names)

# Task №9

# Variant 1

list_multiples_of_eight = [num for num in range(8, 1001, 8)]
print(list_multiples_of_eight)

# Variant 2

list_multiples_of_eight = [num for num in range(8, 1001) if num % 8 == 0]
print(list_multiples_of_eight)

# Task №10

list_of_data = [12, "Snow", 100, "Cars", True, "100"]
index_item = 0

while index_item < len(list_of_data):
    if str(list_of_data[index_item]) == "100":
        print(f"There is a 100 at index no: {index_item}")
    index_item += 1
