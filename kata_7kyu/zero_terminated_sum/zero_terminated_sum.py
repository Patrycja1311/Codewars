def largest_sum(s):
    return max(map(lambda x: sum(map(int, x)), s.split('0')))