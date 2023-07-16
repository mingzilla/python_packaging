if __name__ == '__main__': import __init__; __init__.resolve_root()

import unittest
from src.base_util import value_util


class Test_value_util(unittest.TestCase):

    def test_is_string(self):
        self.assertEqual(value_util.is_string("hello"), True)
        self.assertEqual(value_util.is_string(123), False)
        self.assertEqual(value_util.is_string([1, 2, 3]), False)
        self.assertEqual(value_util.is_string({"key": "value"}), False)


if __name__ == '__main__':
    unittest.main()
