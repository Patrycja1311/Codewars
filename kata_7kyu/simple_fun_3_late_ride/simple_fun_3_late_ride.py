def late_ride(n):
    hours = n // 60
    minutes = n % 60
    return sum(int(digit) for digit in f"{hours:02}{minutes:02}")
