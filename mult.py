import unittest


def multiply(x, y):
    return x + y


class TestMultiply(unittest.TestCase):  # class must be a subclass of unittest.TestCase

    def test_multiply(self):  # name of function must start with test
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, 'should be 50')


# this is how to run unittest or run it by command line 'python3 -m unittest {filename} without .py'
if __name__ == "__main__":
    unittest.main()
