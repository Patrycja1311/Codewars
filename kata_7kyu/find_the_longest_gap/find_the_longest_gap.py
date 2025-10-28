def gap(num):
    return max(map(len, bin(num).strip('0b0').split('1')), default=0)
