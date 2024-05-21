"""Example Class with naming convention"""


class MyExampleClass:
    """MyExampleClass"""

    def __init__(self, field_one, field_two):
        """Constructor"""
        self.field_one = field_one
        self.field_two = field_two

    def public_method(self):
        """Public method that calls the private method and prints the result."""
        result = self.__private_method()
        print(f"Result from private method: {result}")
        return result

    def concat(self, param1):
        """Public method that calls the private method and prints the result."""
        result = self.__private_method()
        return result + " " + param1

    def __private_method(self):
        """Private method that returns a combined value of the two fields."""
        return f"{self.field_one} and {self.field_two}"
