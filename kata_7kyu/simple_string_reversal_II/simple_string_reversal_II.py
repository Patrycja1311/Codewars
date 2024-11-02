def solve(st,a,b):
    return st[:a] + st[a:min(b, len(st)-1)+1][::-1] + st[min(b, len(st)-1)+1:]
