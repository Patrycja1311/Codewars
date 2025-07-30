def reverse_by_center(s):
    return s[(len(s)+1)//2:] + s[len(s)//2] * (len(s)%2) + s[:len(s)//2]
