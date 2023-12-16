def men_from_boys(arr):
    even_num = sorted([num for num in set(arr) if num % 2 == 0])
    odd_num = sorted([num for num in set(arr) if num % 2 != 0], reverse = True)
    return even_num + odd_num
