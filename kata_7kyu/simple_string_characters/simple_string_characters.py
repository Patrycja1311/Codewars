def solve(s):
    return [sum(1 for char in s if char.isupper()),
            sum(1 for char in s if char.islower()),
            sum(1 for char in s if char.isdigit()),
            sum(1 for char in s if not char.isalnum())]
