def jumping_number(number):
    s = str(number)
    return "Jumping!!" if all(abs(int(s[i]) - int(s[i + 1])) == 1 for i in range(len(s) - 1)) else "Not!!"
