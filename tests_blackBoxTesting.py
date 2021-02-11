# Chelsea Satterwhite
# 1/20/21
# CS362 Winter 2021
# HW1: Writing Black Box Tests

# Test Generation Methodology:
# I wrote my test cases by hand before checking them against the TSLgenerator.
# I wrote down the specs for each of the three cards (Visa, Mater, and
# American Express) and made a list of how to break each category for each
# card (categories for the partition testing were prefix, length and check
# digit). From there I wrote tests and created card numbers where only one of
# the three specs was incorrect. I was creating many many mini hypothesis
# that I was then testing (I work in a laboratory - had to connect it to the
# scientific process)

import unittest
from credit_card_validator import credit_card_validator


class TestCreditCard(unittest.TestCase):

    # Testing Input for user errors

    # verifies if card length = 0 / empty string returns false
    # Error Guessing
    # ****************** Triggered testBug1 ******************
    def test_A1(self):
        self.assertFalse(credit_card_validator(""))

    # Testing Valid Card numbers

    # verifies if valid Visa card number returns true
    # Error Guessing - Testing valid input
    # ****************** Triggered testBug3 ******************
    def test_B1(self):
        self.assertTrue(credit_card_validator("4000000000000002"))

    # verifies if valid Master card number 51-55 returns true
    # Error Guessing - Testing valid input
    def test_B2(self):
        self.assertTrue(credit_card_validator("5300000000000006"))

    # verifies if valid Master card number 2221-2720 returns true
    # Error Guessing - Testing valid input
    def test_B3(self):
        self.assertTrue(credit_card_validator("2520000000000007"))

    # verifies if valid American Express card number 34 returns true
    # Error Guessing - Testing valid input
    # ****************** Triggered testBug4 ******************
    def test_B4(self):
        self.assertTrue(credit_card_validator("340000000000009"))

    # verifies if valid American Express card number 37 returns true
    # Error Guessing - Testing valid input
    # ****************** Triggered testBug4 ******************
    def test_B5(self):
        self.assertTrue(credit_card_validator("370000000000002"))

    # Testing Check Digits (Partition Testing for Check Digits)

    # verifies if incorrect Visa card number (correct prefix and length,
    # wrong check digit) returns false
    # Partition Testing
    def test_C1(self):
        self.assertFalse(credit_card_validator("4000000000000001"))

    # verifies if incorrect Master card number 53-55 (correct prefix and
    # length, wrong check digit) returns false
    # Partition Testing
    def test_C2(self):
        self.assertFalse(credit_card_validator("5300000000000005"))

    # verifies if incorrect Master card number 2221-2720 (correct prefix
    # and length, wrong check digit) returns false
    # Partition Testing
    def test_C3(self):
        self.assertFalse(credit_card_validator("2520000000000006"))

    # verifies if incorrect American Express card number 34 (correct prefix
    # and length, wrong check digit) returns false
    # Partition Testing
    # ****************** Triggered testBug4 ******************
    def test_C4(self):
        self.assertFalse(credit_card_validator("340000000000008"))

    # verifies if incorrect American Express card number 37 (correct prefix
    # and length, wrong check digit) returns false
    # Partition Testing
    # ****************** Triggered testBug4 ******************
    def test_C5(self):
        self.assertFalse(credit_card_validator("370000000000001"))

    # Testing Length (Partition Testing for Length)

    # verifies if incorrect Visa card number (correct prefix and check digit,
    # wrong length (15 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    # ****************** Triggered testBug2 ******************
    def test_D1(self):
        self.assertFalse(credit_card_validator("400000000000006"))

    # verifies if incorrect Visa card number (correct prefix and check digit,
    # wrong length (17 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D2(self):
        self.assertFalse(credit_card_validator("40000000000000006"))

    # verifies if incorrect Master card number (correct 51-55 prefix and
    # check digit, wrong length (15 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D3(self):
        self.assertFalse(credit_card_validator("530000000000009"))

    # verifies if incorrect Master card number (correct 51-55 prefix and
    # check digit, wrong length (17 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D4(self):
        self.assertFalse(credit_card_validator("53000000000000009"))

    # verifies if incorrect Master card number (correct 2221-2720 prefix and
    # check digit, wrong length (15 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D5(self):
        self.assertFalse(credit_card_validator("252000000000005"))

    # verifies if incorrect Master card number (correct 2221-2720 prefix and
    # check digit, wrong length (17 instead of 16)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D6(self):
        self.assertFalse(credit_card_validator("25200000000000005"))

    # verifies if incorrect American Express (correct 34 prefix and check
    # digit, wrong length (14 instead of 15)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D7(self):
        self.assertFalse(credit_card_validator("34000000000000"))

    # verifies if incorrect American Express card number (correct 34 prefix
    # and check digit, wrong length (16 instead of 15)) returns false
    # Partition Testing and then Boundary Testing within the partition
    # ****************** Triggered testBug5 ******************
    def test_D8(self):
        self.assertFalse(credit_card_validator("3400000000000000"))

    # verifies if incorrect American Express card number (correct 37 prefix
    # and check digit, wrong length (14 instead of 15)) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_D9(self):
        self.assertFalse(credit_card_validator("37000000000007"))

    # verifies if incorrect American Express card number (correct 37 prefix
    # and check digit, wrong length (16 instead of 15)) returns false
    # Partition Testing and then Boundary Testing within the partition
    # ****************** Triggered testBug5 ******************
    def test_DD1(self):
        self.assertFalse(credit_card_validator("3700000000000007"))

    # Testing Prefix (Partition Testing for Prefix)

    # verifies if incorrect Visa card number (valid length and check digit,
    # wrong prefix < 4) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E1(self):
        self.assertFalse(credit_card_validator("3000000000000004"))

    # verifies if incorrect Visa card number (valid length and check digit,
    # wrong prefix > 4) returns false
    # note: same number as boundary testing on Master card
    # Partition Testing and then Boundary Testing within the partition
    def test_E2(self):
        self.assertFalse(credit_card_validator("5000000000000009"))

    # verifies if incorrect Visa card number (valid length and check digit,
    # wrong prefix > 4) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E3(self):
        self.assertFalse(credit_card_validator("6000000000000007"))

    # verifies if incorrect Master card number 51-55 (valid length and check
    # digit, wrong prefix < 51) returns false
    # note: same number as boundary testing on Visa card
    # Partition Testing and then Boundary Testing within the partition
    def test_E4(self):
        self.assertFalse(credit_card_validator("5000000000000009"))

    # verifies if incorrect Master card number 51-55 (valid length and check
    # digit, wrong prefix > 55) returns false
    # note: same number as boundary testing on Visa card
    # Partition Testing and then Boundary Testing within the partition
    def test_E5(self):
        self.assertFalse(credit_card_validator("5600000000000003"))

    # verifies if incorrect Master card number 2221-2720 (valid length and
    # check digit, wrong prefix < 2221) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E6(self):
        self.assertFalse(credit_card_validator("2220000000000002"))

    # verifies if incorrect Master card number 2221-2720 (valid length and
    # check digit, wrong prefix > 2720) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E7(self):
        self.assertFalse(credit_card_validator("2721000000000004"))

    # verifies if incorrect American Express card number 34 (valid length
    # and check digit, wrong prefix < 34) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E8(self):
        self.assertFalse(credit_card_validator("330000000000001"))

    # verfieis if incorrect American Express card number 34 (valid length
    # and check digit, wrong prefix > 34) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_E9(self):
        self.assertFalse(credit_card_validator("350000000000006"))

    # verifies if incorrect American Express card number 37 (valid length
    # and check digit, wrong prefix < 37) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_EE1(self):
        self.assertFalse(credit_card_validator("360000000000004"))

    # verifies if incorrect American Express card number 37 (valid length
    # and check digit, wrong prefix > 37) returns false
    # Partition Testing and then Boundary Testing within the partition
    def test_EE2(self):
        self.assertFalse(credit_card_validator("380000000000000"))

    # Testing input for MORE user errors (part 2)
    # After reading the hints I realize this part was not needed since were
    # to assume only strings are submitted

    # verifies if valid Visa card number integer instead of string returns
    # false
    # Error Guessing
    def test_A2(self):
        self.assertFalse(credit_card_validator(4000000000000002))

    # verifies if valid Master card number 51-55 integer instead of string
    # returns false
    # Error Guessing
    def test_A3(self):
        self.assertFalse(credit_card_validator(5300000000000006))

    # verifies if valid Master card number 2221-2720 integer instead of
    # string returns false
    # Error Guessing
    def test_A4(self):
        self.assertFalse(credit_card_validator(2520000000000007))

    # verifies if valid American Express card number 34 integer instead of
    # string returns false
    # Error Guessing
    # ****************** Triggered testBug4 ******************
    def test_A5(self):
        self.assertFalse(credit_card_validator(340000000000009))

    # verifies if valid American Express card number 37 integer instead of
    # string returns false
    # Error Guessing
    # ****************** Triggered testBug4 ******************
    def test_A6(self):
        self.assertFalse(credit_card_validator(370000000000002))

    # verifies if zero returns false
    # Error Guessing
    def test_A7(self):
        self.assertFalse(credit_card_validator("0"))

    # Testing the valid Boundaries of Master card ranges
    # I am only testing Master card because the other cards "ranges" have
    # already been tested above in the prefix section

    # verifies if valid Master card number 51-55 (valid length, check digit,
    # and prefix 51) returns true
    # Boundary Testing
    def test_EE3(self):
        self.assertTrue(credit_card_validator("5100000000000007"))

    # verifies if valid Master card number 51-55 (valid length, check digit,
    # and prefix 55) returns true
    # Boundary Testing
    def test_EE4(self):
        self.assertTrue(credit_card_validator("5500000000000004"))

    # verifies if valid Master card number 2221-2720 (valid length, check
    # digit, and prefix 2221) returns true
    # Boundary Testing
    def test_EE5(self):
        self.assertTrue(credit_card_validator("2221000000000009"))

    # verifies if valid Master card number 2221-2720 (valid length, check
    # digit, and prefix 2720) returns true
    # Boundary Testing
    # ****************** Triggered testBug6 ******************
    def test_EE6(self):
        self.assertTrue(credit_card_validator("2720000000000005"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
