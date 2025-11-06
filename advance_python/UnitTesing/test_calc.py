import unittest
from calc import add,divide


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
        self.assertNotEqual(add(9,9),0)
    
    def test_divide(self):
        self.assertEqual(divide(10,2),5)
        with self.assertRaises(ValueError):
            divide(10,0)

if __name__=="__main__":
    unittest.main()



