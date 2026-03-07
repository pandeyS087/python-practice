# Palindrome Checker

def is_palindrome(text):
    # Remove spaces and make lowercase for consistency
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

# Example usage
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")