def unused_digits(*numbers):
    return ''.join(sorted(set("0123456789") - set(''.join(map(str, numbers)))))
