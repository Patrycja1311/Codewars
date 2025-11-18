def double_check(strng):
    strng = strng.lower()
    return any(strng[i] == strng[i+1] for i in range(len(strng)-1))
