def next_happy_year(year):
    year += 1
    while not all(str(year).count(digit) == 1 for digit in str(year)):
        year += 1
    return year
