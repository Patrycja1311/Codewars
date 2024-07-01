def sort_vowels(s):
    if not isinstance(s, str): return ""
    return "\n".join(f"|{char}" if char in "aeiouAEIOU" else f"{char}|" for char in s)
