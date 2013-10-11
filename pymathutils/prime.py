"""
Checks if a number is a prime number by 
checking if it divides evenly by itself and 1.

"""

def isprime(n):
    """Check if number is prime."""
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max = n**0.5+1
    i = 3
    
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True
