def number_of_sigfigs(number):
    if '.' in number:
        number = number.lstrip('0')
        number = number.replace('.', '')
        number = number.lstrip('0')
        return len(number) or 1
    return len(number.lstrip('0').rstrip('0'))
