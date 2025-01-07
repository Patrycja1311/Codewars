def substring_test(s1, s2):
    s1, s2 = s1.lower(), s2.lower()
    substrings = set(s1[i:i+2] for i in range(len(s1) - 1))
    return any(sub in s2 for sub in substrings)
