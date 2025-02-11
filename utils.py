def calculate_factorial(n: int) -> int:
    """
    Calculate factorial of a given number.
    
    Args:
        n: A positive integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

<<<<<<< HEAD
def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1
=======
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

>>>>>>> 2bb65dc1754d0029140186fd557821a6bfb31b96
