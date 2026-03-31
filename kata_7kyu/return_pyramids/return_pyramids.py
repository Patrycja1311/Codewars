def pyramid(n):
    return '/\\\n' if n == 1 else '\n'.join(' '*(n-i-1) + '/' + ' '*(2*i) + '\\' for i in range(n-1)) + '\n' + '/' + '_'*(2*(n-1)) + '\\\n'
