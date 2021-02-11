# Chelsea Satterwhite
# 2/1/21
# CS362 Winter 2021
# HW3: Random Testing Hands On

from unittest import TestCase
import unittest
from credit_card_validator import credit_card_validator
# Need for randint and choice
import random


class TestCreditCard(unittest.TestCase):

    # testing credit cards of length 16
    def test_rand16(self):
        # All possible credit card prefixes
        prefixes = [4, 51, 55, 2221, 2720, 34, 37]
        length = 16
        for i in range(0, 550000):
            # picks a random edge case
            chance_edge_cases = random.randint(0, 2)
            # keeps the edge case the same as the array
            if chance_edge_cases == 0:
                prefix = random.choice(prefixes)
            # generates a number -1 the picked edge case
            elif chance_edge_cases == 1:
                prefix = random.choice(prefixes)
                prefix -= 1
            # generates a number +1 the picked edge case
            else:
                prefix = random.choice(prefixes)
                prefix += 1
            # credit: GeeksforGeeks - Generate random string of given length
            # https://www.geeksforgeeks.org/python-generate-random-string-of
            # -given-length/
            # fill the rest of the credit card number with random ints
            # and convert to string
            end_card_numbers = ''.join(
                ["{}".format(random.randint(0, 9)) for num in range
                    (0, length-len(str(prefix)))])
            # convert the prefix into a string and join the string of numbers
            rand_creditcard = str(prefix) + end_card_numbers
            credit_card_validator(str(rand_creditcard))

    # Testing credit cards of length 15
    # same as the above code but length = 15 and fewer tests run
    def test_rand15(self):
        prefixes = [4, 51, 55, 2221, 2720, 34, 37]
        length = 15
        for i in range(0, 5000):
            chance_edge_cases = random.randint(0, 2)
            if chance_edge_cases == 0:
                prefix = random.choice(prefixes)
            elif chance_edge_cases == 1:
                prefix = random.choice(prefixes)
                prefix -= 1
            else:
                prefix = random.choice(prefixes)
                prefix += 1
            end_card_numbers = ''.join(
                ["{}".format(random.randint(0, 9)) for num in range(
                    0, length-len(str(prefix)))])
            rand_creditcard = str(prefix) + end_card_numbers
            credit_card_validator(str(rand_creditcard))

if __name__ == '__main__':
    unittest.main(verbosity=2)
