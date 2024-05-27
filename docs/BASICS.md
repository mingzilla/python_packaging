## Naming - Class

```python 
# my_example_class.py
class MyExampleClass:
    static_field = "static field"
    _static_field = "protected static field"
    __static_field = "private static field"

    def __init__(self, name):
        self.public_field = MyExampleClass.static_field + name
        self._protected_field = MyExampleClass._static_field
        self.__private_field = MyExampleClass.__static_field

    def public_method(self):
        return

    def _protected_method(self):
        return

    def __private_method(self):
        return

    @staticmethod
    def public_static_method(x: int, y: int) -> int:
        return x + y


if __name__ == "__main__":
    obj = MyExampleClass("hi")
    MyExampleClass.public_static_method(1, 2)

```

## Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)


class Teacher(Person):
    def __init__(self, name, subject):
        self.subject = subject

        Person.__init__(self, name)

```

## Function

* how to write a function
* how to provide typing

```python
def calculate_minutes(seconds: int) -> float:
    minutes: float = seconds / 60  # variable creation does not need an extra keyword
    return minutes

```

## lambda function

* why? one line

```python
add_two = lambda x: x + 2
add_two(5)

```

## Casting

```python
temperature: str = str(97.5)  # casting
type(temperature)  # prints str
```

## Data Types

| Type    | Casting  |
|---------|----------|
| int     | int(v)   |
| float   | float(v) |
| boolean | bool(v)  |
| str     | str(v)   |

## Logical Operators

* general operator is just like js
* logical operators are as below

| Operator | Example               |
|----------|-----------------------|
| and      | x > 2 and y == 1      |
| or       | x > 3 or y > 5        |
| not      | not(x > 10 and y > 5) |

## if, elif, else

```python
score = 70

if score >= 80:
    print("big")

elif score > 65:
    print("mid")

else:
    print("small")

```

## for loop

```python

for num in [1, 2, 3, 4, 5]:
    print(num)

for i in range(3):
    print(i)
```

## mapping function

```python
# square = lambda x: x**2
def square(x):
    return x ** 2


numbers = [1, 2, 3]

result = map(square, numbers)

result_list = list(result)  # Convert to a list - [1, 4, 9]

```

## filter function

```python
# myFn = lambda x: x > 2
def myFn(x) -> bool:
    return x > 2


numbers = [1, 2, 3, 4, 5]

result = filter(myFn, numbers)

result_list = list(result)  # Convert to a list - [3, 4, 5]

```

## try, except, finally

```python
try:
    print(sum([1, 2, 3]))

except:
    print("Error")

finally:
    print("Done")

```
