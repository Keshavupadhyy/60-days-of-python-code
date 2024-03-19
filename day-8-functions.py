def sum_of_digits(number):
    """Function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(abs(number)))

# Example usage:
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")
