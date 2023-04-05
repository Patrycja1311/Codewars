def descending_order(num):
    digit = list(str(num))
    digit.sort(reverse=True)
    digits_string = int("".join(digit))
    return(digits_string)
