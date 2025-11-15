import unittest
from calc3 import add,divide,even
class TestCalc3(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(1,2),4)

    def test_divide(self):
        self.assertEqual(divide(10,2),5.0)
        with self.assertRaises(ValueError):
            divide(5,0)
    # def test_even(self):