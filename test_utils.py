# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(2), 2.0)
        self.assertEqual(utils.fact(4), 24.0)
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,1,-2), (-2.0, 1.0))
        self.assertEqual(utils.roots(1,-2,0), (0.0,2.0))
        pass
    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
