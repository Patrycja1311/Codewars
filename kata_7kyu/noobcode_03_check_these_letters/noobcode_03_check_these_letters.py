def letter_check(arr):
    a, b = arr[0].lower(), arr[1].lower()
    return all(ch in a for ch in b)
