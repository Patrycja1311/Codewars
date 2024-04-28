def digits(num):
    return [int(str(num)[i]) + int(str(num)[j]) for i in range(len(str(num))) for j in range(i+1, len(str(num)))]
