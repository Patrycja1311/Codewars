def least_larger(a, i):
    return min((j for j in range(len(a)) if a[j] > a[i]), default=-1, key=lambda j: a[j])
