def product_array(numbers):
    total_product = 1
    for num in numbers:
        total_product *= num
    return [total_product // num for num in numbers]
