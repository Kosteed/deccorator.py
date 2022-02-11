# Task #1:

    Write a Python program to triple all numbers of a given list of integers. Use Python map.

# Task #2:

    Write a decorator which wraps functions to log function arguments and the return value on each call. Provide support for both positional and named arguments 
    (your wrapper function should take both *args and **kwargs and print them both):

# Task #3:
    
    write a function that should print a list of users accepted as an argument. Write a decorator for this function that 
    checks the length of the username and if it is less than 5 , the user should not be added to the list. 
    To filter in the decorator, use the filter function.

# Task #4:
    
    write a memoized decorator that caches function calls. Create a global MEMO variable of type dict. Write two functions, 
    one to multiply numbers and the other to divide. Implement the decorator so that the first two function calls you see 
    that they are called, then call. them two more times and make sure that the values were taken from the dictionary. 
    Hint, you can check the values in the dictionary and store them using func.__name__ 
