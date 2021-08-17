from unittest import TestCase
from algorithms import reverse_str, isPalindrome, factorial


class AlgorithmsTestCase2(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('hello'), 'olleh')
        self.assertEqual(reverse_str('Apple'), 'elppA')

    def test_is_palindrome(self):
        self.assertTrue(isPalindrome('racecar'))
        # Should ignore casing
        self.assertTrue(isPalindrome('Racecar'))
        self.assertTrue(isPalindrome('wow'))
        self.assertFalse(isPalindrome('dog'))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertRaises(ValueError, factorial, -5)
        self.assertRaises(ValueError, factorial, 4.3)
