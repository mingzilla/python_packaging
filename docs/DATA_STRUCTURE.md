# Summary

* list
* dictionary
* typing
* function as type

## List

* create a list and assign 2 values [1, 2] in one line
* add an item to a list
* get an item from a list at index
* remove an item from a list
* remove an item at a certain index from a list
* lambda map function on a list, e.g. a list [1, 2] runs a map function to add 1 to each item
* lambda filter function on a list, e.g. return odd numbers only

```python
# 1. Create a list and assign 2 values [1, 2] in one line
my_list = [1, 2]

# 2. Add an item to a list
my_list.append(3)
# my_list is now [1, 2, 3]

# 3. Remove an item from a list
my_list.remove(2)
# my_list is now [1, 3]

# 4. Remove an item at a certain index from a list
item = my_list[1]  # getting item
del my_list[1]
# my_list is now [1]

# Re-assign for the next examples
my_list = [1, 2]

# 5. Lambda map function on a list (e.g., add 1 to each item)
mapped_list = list(map(lambda x: x + 1, my_list))
# mapped_list is now [2, 3]

# Re-assign for the next example
my_list = [1, 2, 3, 4, 5]

# 6. Lambda filter function on a list (e.g., return odd numbers only)
filtered_list = list(filter(lambda x: x % 2 != 0, my_list))
# filtered_list is now [1, 3, 5]
```

## Dictionary

* create a dictionary and assign 2 values {'x': 1, 'y': 2} in one line
* add an item to a dictionary
* get an item from a dictionary
* remove an item from a dictionary
* get all the keys from a dictionary
* get all the values from a dictionary
* lambda map function on a dictionary, so that each value `+1`
* lambda filter function on a dictionary, e.g. return entries that are odd numbers

```python
# 1. Create a dictionary and assign 2 values [x: 1, y: 2] in one line
my_dict = {'x': 1, 'y': 2}

# 2. Add an item to a dictionary
my_dict['z'] = 3
# my_dict is now {'x': 1, 'y': 2, 'z': 3}

# 3. Get an item from a dictionary
value = my_dict['x']
# value is 1

# 4. Remove an item from a dictionary
del my_dict['y']
# my_dict is now {'x': 1, 'z': 3}

# 5. Get all the keys from a dictionary
keys = list(my_dict.keys())
# keys is ['x', 'z']

# 6. Get all the values from a dictionary
values = list(my_dict.values())
# values is [1, 3]

# 7. Lambda map function on a dictionary (each value +1)
mapped_dict = {k: v + 1 for k, v in my_dict.items()}
# mapped_dict is {'x': 2, 'z': 4}

# 8. Lambda filter function on a dictionary (return entries that are odd numbers)
filtered_dict = {k: v for k, v in my_dict.items() if v % 2 != 0}
# filtered_dict is {'x': 1, 'z': 3}
```

The following are the same

```python
my_dict = {'x': 1, 'y': 2}


### Approach 1
def complex_operation(x):
    return x ** 2 + 3


mapped_dict1 = {k: complex_operation(v) for k, v in my_dict.items()}

### Approach 2
### The keyword `lambda` makes an inline function
mapped_dict2 = {k: (lambda x: x ** 2 + 3)(v) for k, v in my_dict.items()}
```

## Typing

* param: x can be str or int
* param: y can only be int
* return: -> type

```python
from typing import Union


def my_function(x: Union[str, int], y: int) -> int:
    if isinstance(x, int):
        return x + y
    elif isinstance(x, str):
        return int(x) + y  # Convert the string to an integer before adding y
    else:
        raise ValueError("Parameter x must be a string or an integer")


# Example usage:
result1 = my_function(5, 3)  # Output: 8
result2 = my_function("5", 3)  # Output: 8

```

### function as param with typing

```python
from typing import Callable


def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    """Apply the specified operation to x and y."""
    return operation(x, y)


# Example usage:
def add(x: int, y: int) -> int:
    """Add two integers."""
    return x + y


def subtract(x: int, y: int) -> int:
    """Subtract y from x."""
    return x - y


result1 = apply_operation(5, 3, add)  # Output: 8
result2 = apply_operation(5, 3, subtract)  # Output: 2
```