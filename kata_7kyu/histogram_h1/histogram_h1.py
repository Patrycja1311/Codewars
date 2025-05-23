def histogram(results):
    return ''.join(f"{i}|{'#'*results[i-1]}{' ' + str(results[i-1]) if results[i-1] else ''}\n" for i in range(6, 0, -1))
