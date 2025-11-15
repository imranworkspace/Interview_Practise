from calc2 import add,divide,evend
import unittest

# python -m unittest test_calc2.py

class TestCal2(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertNotEqual(add(5,5),9)
    
    def test_divide(self):
        self.assertNotEqual(divide(10,2),6)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_evend(self):
        self.assertTrue(evend(10))
        self.assertFalse(evend(11))

if __name__=="__main__":
    unittest.main()
