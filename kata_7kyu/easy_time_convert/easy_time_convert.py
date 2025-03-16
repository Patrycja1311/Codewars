def time_convert(num):
    return "00:00" if num <= 0 else f"{num//60:02}:{num%60:02}"
