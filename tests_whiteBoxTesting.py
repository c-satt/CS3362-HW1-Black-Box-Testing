# Chelsea Satterwhite
# 1/20/21
# CS362 Winter 2021
# HW1: Writing Black Box Tests

# Logic behind the conditional statements to figure out the 7 tests
# 		|
# 	 -------
#   |	A	|-- T (1)
# 	 -------
# 		| F (2)
# 	 -------  	  -------
# 	|	B	|----|	 C	 |-- T (3)
# 	 -------   T  -------
# 		| F (5)	 	 |
# 	 -------		 F (4)
# 	|	D	|-- T (6)
# 	 -------
# 		|
# 		F (7)
#
# Since statement B must return true to get to the nested statement C, that
# branch is covered in statement C (val == 6 or not) returning true and false
# so we don't need to write a test specifically for that statement (there is
# not a single return statement for this condition)

# This line allowed me to get full branch coverage on PyCharm
# Before this line was added only 10% coverage
from unittest import TestCase
# Normal imports similar to HW1
import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    # Verifies path 1 is reached by statement A returning True
    # Conditional Statement C1
    def test1(self):
        self.assertTrue(contrived_func(145))

    # Verifies path 2 is reached by statement A returning False
    # Conditional Statements C3, C6, and C10
    def test2(self):
        self.assertFalse(contrived_func(152))

    # Verifies path 3 is reached by statement A returning False, statement B
    # returning True, and statement C returning False
    # Conditional Statements C2, C4 and C7
    def test3(self):
        self.assertFalse(contrived_func(6))

    # Verifies path 4 is reached by statement A returning False, statement B
    # returning True, and statement C returning True
    # Conditional Statements C2, C4, and C8
    def test4(self):
        self.assertTrue(contrived_func(5))

    # Verifies path 5 is reached by statement A returning False, statement B
    # returning False (since there is another conditional statement here, the
    # program continues to evaluate)
    # Conditional Statements C3, C6, and C9
    def test5(self):
        self.assertFalse(contrived_func(360))

    # Verifies path 6 is reached by statement A returning False, statement B
    # returning False, and statement D returning True
    # Conditional Statements C2, C6, and C11
    def test6(self):
        self.assertTrue(contrived_func(75))

    # Verifies path 7 is reached by statement A returning False, statement B
    # returning False, and statement D returning False
    # Conditional Statements C2, C5 and C12
    def test7(self):
        self.assertFalse(contrived_func(51))

if __name__ == '__main__':
    unittest.main(verbosity=2)
