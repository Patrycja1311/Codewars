def eq_sum_powdig(h_max, exp):
    return [n for n in range(2, h_max + 1) if n == sum(int(d)**exp for d in str(n))]
