def short_form(s):
    vowels = "aeiouAEIOU"
    return s if len(s) <= 2 else s[0] + ''.join(c for c in s[1:-1] if c not in vowels) + s[-1]
