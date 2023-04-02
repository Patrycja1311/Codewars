def find_uniq(arr):
    arr.sort()
    y = len(arr)
    first_unknow = arr[0]
    last_unknow = arr[y-1]
    x = arr.count(first_unknow)
    y = arr.count(last_unknow)
    if x == 1:
        return first_unknow
    elif y == 1:
        return last_unknow
