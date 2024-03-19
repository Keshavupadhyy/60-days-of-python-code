def is_palindrome(word):
    """Function to check if a word is a palindrome."""
    return word == word[::-1]

# Example usage:
word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
