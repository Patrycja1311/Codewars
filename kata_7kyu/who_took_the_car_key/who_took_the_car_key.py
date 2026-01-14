def who_took_the_car_key(message):
    return ''.join(chr(int(b, 2)) for b in message)
