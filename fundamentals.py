"""Small examples of Python fundamentals."""


def add_numbers(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def average(numbers: list[float]) -> float:
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


def is_palindrome(text: str) -> bool:
    """Return True when text reads the same forwards and backwards."""
    cleaned_text = "".join(
        character.lower() for character in text if character.isalnum()
    )
    return cleaned_text == cleaned_text[::-1]


def is_prime(number: int) -> bool:
    """Return True when number is a prime number."""
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


if __name__ == "__main__":
    print("2 +3 =", add_numbers(2, 3))
    print("25     C =", celsius_to_fahrenheit(25), "F")
    print("Average:", average([10, 20, 30]))
    print("'Level' is a palindrome:", is_palindrome("Level"))
    print("7 is prime:", is_prime(7))
