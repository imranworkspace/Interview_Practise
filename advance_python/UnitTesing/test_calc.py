import unittest
from calc import add,divide,even

# python -m unittest test_calc2.py

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,5),7)
        self.assertNotEqual(add(5,5),9)

    
    def test_divide(self):
        self.assertEqual(divide(10,2),5)
        
        with self.assertRaises(ValueError):
            divide(10,0)

    def test_even(self):
        self.assertTrue(even(10))
        self.assertFalse(even(30))

if __name__=="__main__":
    unittest.main()