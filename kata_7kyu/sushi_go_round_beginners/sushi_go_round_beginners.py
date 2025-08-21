def total_bill(s):
    reds = s.count("r")
    payable = reds - reds // 5
    return payable * 2