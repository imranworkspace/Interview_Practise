import unittest
from calc5 import add,prime

class Test_Add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        # self.assertNotEqual(add(2,3),5)
    
    def test_prime(self):
        self.assertTrue(prime(2),True)
        self.assertFalse(prime(12),False)
        self.assertTrue(prime(97),False)
        
     