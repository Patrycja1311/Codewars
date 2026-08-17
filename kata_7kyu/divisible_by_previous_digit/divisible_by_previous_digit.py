def divisible_by_last(n):
    n = str(n)
    return [False] + [int(n[i]) % int(n[i-1]) == 0 if n[i-1] != '0' else False
                      for i in range(1, len(n))]
