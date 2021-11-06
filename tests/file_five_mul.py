# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from sample.simple import add_one
from sample.simple import multiply

# Multiplication Code:
class TestSimple(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(5, 4), 20)



if __name__ == '__main__':
    unittest.main()
