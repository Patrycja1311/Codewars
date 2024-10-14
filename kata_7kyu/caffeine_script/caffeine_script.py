def caffeine_buzz(n):
    result = "mocha_missing!"
    if n % 3 == 0:
        result = "Coffee" if n % 4 == 0 else "Java"
        if n % 2 == 0:
            result += "Script"
    return result
