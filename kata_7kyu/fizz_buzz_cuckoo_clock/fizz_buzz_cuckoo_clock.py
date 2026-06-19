def fizz_buzz_cuckoo_clock(time):
    h, m = map(int, time.split(':'))
    if m == 0:
        hour = h % 12
        if hour == 0:
            hour = 12
        return ' '.join(['Cuckoo'] * hour)
    if m == 30:
        return 'Cuckoo'
    result = []
    if m % 3 == 0:
        result.append('Fizz')
    if m % 5 == 0:
        result.append('Buzz')
    return ' '.join(result) if result else 'tick'
