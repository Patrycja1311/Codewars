def determine_time(arr):
    return sum(int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in (t.split(":") for t in arr)) <= 86400
