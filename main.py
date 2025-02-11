from utils import calculate_factorial

def main() -> None:
    try:
        number = 5
        result = calculate_factorial(number)
        print(f"Factorial of {number} is {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 