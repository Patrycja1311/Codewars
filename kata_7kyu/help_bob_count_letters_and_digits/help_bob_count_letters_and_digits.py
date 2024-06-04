def count_letters_and_digits(s: str) -> int:
    return sum(char.isalnum() for char in s)
