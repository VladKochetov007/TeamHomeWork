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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

