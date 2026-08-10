def cool_string(s):
    if not s.isalpha():
        return False

    for i in range(len(s) - 1):
        if s[i].islower() == s[i + 1].islower():
            return False

    return True

