from typing import NoReturn, List


def find_sum(input_data: list) -> NoReturn:
    """
    Find the sum of all numbers in a list
    :param input_data: List of mixed data type
    """
    res_sum = 0
    for data in input_data:
        if isinstance(data, (int, float)):
            res_sum += data
    print(f"Sum of all numbers in {input_data} is {res_sum}")


def find_even_sum(input_data: list) -> NoReturn:
    """
    Find the sum of all even numbers in a list
    :param input_data: List of mixed data type
    """
    res_sum = 0
    for data in input_data:
        if isinstance(data, int) and data % 2 == 0:
            res_sum += data
    print(f"Sum of all even numbers in {input_data} is {res_sum}")


def find_int(input_data: tuple) -> NoReturn:
    """
    Print only integer values
    :param input_data: List of mixed data type
    """
    for data in input_data:
        if isinstance(data, int):
            print(f"Find {data} in {input_data}")


def print_tuple(input_data: list) -> NoReturn:
    """
    Apply enumerate() and print elements in a tuple
    :param input_data: List of mixed data type
    """
    for data in enumerate(input_data):
        print(f"{data} in {input_data}")


def print_keys(input_data: dict) -> NoReturn:
    """
    Print all keys in a dictionary
    :param input_data: Dictionary
    """
    for key in input_data.keys():
        print(f"Key {key} in {input_data}")


def print_keys_val(input_data: dict) -> NoReturn:
    """
    Print both keys and values from a dictionary
    :param input_data: Dictionary
    """
    for key in input_data.keys():
        print(f"Key {key} and value {input_data[key]} in {input_data}")


def find_fruits_num(fruits: list) -> NoReturn:
    """
    Print out the number of the fruits in the list
    :param fruits: List of fruits type
    """
    fruits_storage = {'apple': 20, 'lemon': 30, 'orange': 40, 'pineapple': 50, 'mango': 60}
    fruits_type = [fruit_type.lower() for fruit_type in fruits]
    for fruit in fruits_type:
        if fruit in fruits_storage.keys():
            print(f"Number of {fruit} is {fruits_storage[fruit]}")


def append_names(names: list) -> NoReturn:
    """
    Append each item of the list with a Dr. prefix to the new list
    :param names: List of names
    """
    new_names = []
    for name in names:
        new_names.append('Dr.' + name)


def find_div_int() -> List[int]:
    """
    Find all numbers from 1-1000 that are divisible by 8
    :return: List all numbers from 1-1000 are divisible by 8
    """
    return [num for num in range(1, 1001) if num % 8 == 0]


def find_num(input_data: list) -> NoReturn:
    """
    Iterate through the list and if there is 100, print it with its index
    :param input_data: List of mixed data type
    """
    ind = 0
    while ind < input_data.__len__():
        if isinstance(input_data[ind], int) and input_data[ind] == 100:
            print(f"There is 100 at index {ind}")
        ind += 1


random_data = ['German', 10, ('Denis', 36), 24.5, 57, 100, 'Oleg', 38, 9.5]
mixed_data = (25, ('Vita', 'Alex'), 13.7, 43, 'Oleg', {'age': 23, 'name': 'Denis'})
person_data = {'name': 'German', 'age': 25, 'job': 'programmer'}
fruits_data = ['grapefruit', 'LEMON', 'mango', 'Persimmon', 'Pineapple']
names_data = ['German', 'Denis', 'Oleg', 'Vita', 'Kate']

find_sum(random_data)

find_even_sum(random_data)

find_int(mixed_data)

print_tuple(fruits_data)

print_keys(person_data)

print_keys_val(person_data)

find_fruits_num(fruits_data)

append_names(names_data)

result = find_div_int()

find_num(random_data)
