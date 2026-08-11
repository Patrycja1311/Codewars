def rounders(value):
    while len(str(value).rstrip("0")) > 1:
        s = list(str(value))
        i = len(s) - 1

        while s[i] == "0":
            i -= 1

        if int(s[i]) >= 5:
            s[i] = "0"
            j = i - 1
            while j >= 0 and s[j] == "9":
                s[j] = "0"
                j -= 1
            if j >= 0:
                s[j] = str(int(s[j]) + 1)
            else:
                s.insert(0, "1")
        else:
            s[i] = "0"

        value = int("".join(s))

    return value
