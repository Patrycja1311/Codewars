def solve(s):
    upper_letter = sum(1 for char in s if char.isupper())
    lower_letter = sum(1 for char in s if char.islower())
    return s.upper() if lower_letter < upper_letter else s.lower()
