def stray(arr):
    for i in arr:
        number_occurrences = arr.count(i)
        if number_occurrences == 1:
            return i
