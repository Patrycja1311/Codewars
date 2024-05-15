def no_ifs_no_buts(a, b):
    return str(a) + " is " + ("equal to " + str(b), "greater than " + str(b), "smaller than " + str(b))[2 * (a < b) + (a > b)]
