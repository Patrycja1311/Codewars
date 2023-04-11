def square_digits(num):
    text = str(num)
    digit_text = list(text)
    square_number_digits = []
    for number in digit_text:
        digit = int(number)
        square_number_digits.append(digit ** 2)
        str_square_number_digits = [str(int_num) for int_num in square_number_digits]
        string_square_number_digits = "".join(str_square_number_digits)
    return int(string_square_number_digits)
