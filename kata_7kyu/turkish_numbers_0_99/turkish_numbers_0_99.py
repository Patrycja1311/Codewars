def get_turkish_number(num):
    numbers = ['sıfır', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
    num_above = ['', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
    if num < 10:
        return numbers[num]
    elif num % 10 == 0:
        return num_above[num // 10]
    else:
        return num_above[num // 10] + ' ' + numbers[num % 10]
