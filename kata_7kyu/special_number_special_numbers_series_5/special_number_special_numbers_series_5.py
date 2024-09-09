def special_number(number):
    return "Special!!" if all(d in '012345' for d in str(number)) else "NOT!!"
