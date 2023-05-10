def count(s):
    letter_counts = {}
    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts
