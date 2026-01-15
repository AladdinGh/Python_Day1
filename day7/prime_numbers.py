"""
Prime Numbers Finder
This script finds all prime numbers between 1 and 250,
displays them, and saves the results to a file.
"""

def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num: Integer to check
        
    Returns:
        Boolean: True if prime, False otherwise
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    # Check odd divisors up to square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def find_primes(start, end):
    """
    Find all prime numbers in the given range.
    
    Args:
        start: Starting number (inclusive)
        end: Ending number (inclusive)
        
    Returns:
        List of prime numbers in the range
    """
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes


def main():
    """Main function to find primes and save to file."""
    start = 1
    end = 250
    
    # Find all prime numbers
    primes = find_primes(start, end)
    
    # Display results to console
    print(f"Prime numbers between {start} and {end}:")
    print(f"Total count: {len(primes)}\n")
    print("Primes:")
    print(primes)
    
    # Save results to file
    results_file = "results.txt"
    try:
        with open(results_file, "w") as f:
            f.write(f"Prime Numbers Between {start} and {end}\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Total count: {len(primes)}\n\n")
            f.write("Prime numbers:\n")
            f.write(str(primes) + "\n\n")
            f.write("Formatted list (one per line):\n")
            for prime in primes:
                f.write(f"{prime}\n")
        
        print(f"\n✓ Results saved to '{results_file}'")
    except IOError as e:
        print(f"✗ Error writing to file: {e}")


if __name__ == "__main__":
    main()
