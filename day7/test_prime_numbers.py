"""
Unit Tests for Prime Numbers Script
Tests the is_prime() and find_primes() functions
"""

import unittest
import sys
from io import StringIO
from prime_numbers import is_prime, find_primes


class TestIsPrime(unittest.TestCase):
    """Test cases for the is_prime() function"""
    
    def test_prime_numbers(self):
        """Test that known prime numbers return True"""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime), f"{prime} should be prime")
    
    def test_non_prime_numbers(self):
        """Test that known non-prime numbers return False"""
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 15, 20, 25, 30, 100]
        for non_prime in non_primes:
            with self.subTest(non_prime=non_prime):
                self.assertFalse(is_prime(non_prime), f"{non_prime} should not be prime")
    
    def test_negative_numbers(self):
        """Test that negative numbers are not prime"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-100))
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertFalse(is_prime(0), "0 is not prime")
        self.assertFalse(is_prime(1), "1 is not prime")
        self.assertTrue(is_prime(2), "2 is prime (smallest prime)")
    
    def test_large_primes(self):
        """Test larger prime numbers"""
        large_primes = [239, 241, 223, 227, 229]
        for prime in large_primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))
    
    def test_large_non_primes(self):
        """Test larger non-prime numbers"""
        non_primes = [240, 242, 225, 228, 230]
        for non_prime in non_primes:
            with self.subTest(non_prime=non_prime):
                self.assertFalse(is_prime(non_prime))


class TestFindPrimes(unittest.TestCase):
    """Test cases for the find_primes() function"""
    
    def test_find_primes_1_to_10(self):
        """Test finding primes between 1 and 10"""
        expected = [2, 3, 5, 7]
        result = find_primes(1, 10)
        self.assertEqual(result, expected)
    
    def test_find_primes_1_to_20(self):
        """Test finding primes between 1 and 20"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = find_primes(1, 20)
        self.assertEqual(result, expected)
    
    def test_find_primes_1_to_250(self):
        """Test finding primes between 1 and 250"""
        result = find_primes(1, 250)
        self.assertEqual(len(result), 53, "There should be 53 primes between 1 and 250")
        self.assertEqual(result[0], 2, "First prime should be 2")
        self.assertEqual(result[-1], 241, "Last prime up to 250 should be 241")
    
    def test_find_primes_range_all_prime(self):
        """Test range where all numbers are prime"""
        result = find_primes(2, 3)
        self.assertEqual(result, [2, 3])
    
    def test_find_primes_range_no_primes(self):
        """Test range with no primes"""
        result = find_primes(24, 28)
        self.assertEqual(result, [])
    
    def test_find_primes_single_number_prime(self):
        """Test single number that is prime"""
        result = find_primes(7, 7)
        self.assertEqual(result, [7])
    
    def test_find_primes_single_number_not_prime(self):
        """Test single number that is not prime"""
        result = find_primes(4, 4)
        self.assertEqual(result, [])
    
    def test_find_primes_returns_list(self):
        """Test that find_primes returns a list"""
        result = find_primes(1, 50)
        self.assertIsInstance(result, list)
    
    def test_find_primes_ordered(self):
        """Test that primes are returned in ascending order"""
        result = find_primes(1, 100)
        self.assertEqual(result, sorted(result))
    
    def test_find_primes_no_duplicates(self):
        """Test that there are no duplicate primes"""
        result = find_primes(1, 100)
        self.assertEqual(len(result), len(set(result)))


class TestPrimeProperties(unittest.TestCase):
    """Test mathematical properties of primes"""
    
    def test_all_primes_greater_than_1(self):
        """All primes should be greater than 1"""
        primes = find_primes(1, 250)
        for prime in primes:
            self.assertGreater(prime, 1)
    
    def test_even_primes_only_2(self):
        """Only 2 should be an even prime"""
        primes = find_primes(1, 250)
        even_primes = [p for p in primes if p % 2 == 0]
        self.assertEqual(even_primes, [2])
    
    def test_all_others_odd(self):
        """All primes except 2 should be odd"""
        primes = find_primes(1, 250)
        odd_primes = [p for p in primes if p > 2]
        for prime in odd_primes:
            self.assertEqual(prime % 2, 1, f"{prime} should be odd")


if __name__ == "__main__":
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestIsPrime))
    suite.addTests(loader.loadTestsFromTestCase(TestFindPrimes))
    suite.addTests(loader.loadTestsFromTestCase(TestPrimeProperties))
    
    # Create a test runner that writes to both console and file
    results_file = "test_results.txt"
    
    with open(results_file, "w", encoding="utf-8") as f:
        # Run tests with verbose output
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)
        
        # Add summary to file
        f.write("\n" + "="*70 + "\n")
        f.write("TEST SUMMARY\n")
        f.write("="*70 + "\n")
        f.write(f"Tests Run: {result.testsRun}\n")
        f.write(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}\n")
        f.write(f"Failures: {len(result.failures)}\n")
        f.write(f"Errors: {len(result.errors)}\n")
        
        if result.wasSuccessful():
            f.write("\nRESULT: ALL TESTS PASSED (PASS)\n")
        else:
            f.write("\nRESULT: SOME TESTS FAILED (FAIL)\n")
    
    # Also print to console
    print(f"\nTest results written to '{results_file}'")
