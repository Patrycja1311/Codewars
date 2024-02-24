def switcher(arr):
    alphabet = 'zyxwvutsrqponmlkjihgfedcba!? '
    result = ''
    for num in arr:
        letter = alphabet[int(num) - 1]
        result += letter
    return result
