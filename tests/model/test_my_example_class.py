"""TestMyExampleClass"""

import unittest

from src.model.my_example_class import MyExampleClass


class TestMyExampleClass(unittest.TestCase):
    """TestValueUtil"""

    def test_public_method(self):
        """test_is_string"""
        example_instance = MyExampleClass("value1", "value2")
        self.assertEqual(example_instance.public_method(), "value1 and value2")
        self.assertEqual(example_instance.concat("Hi"), "value1 and value2 Hi")


if __name__ == "__main__":
    unittest.main()
