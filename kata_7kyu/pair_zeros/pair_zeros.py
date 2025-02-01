def pair_zeros(arr):
    result, zero_count = [], 0
    for num in arr:
        if num == 0:
            zero_count += 1
            if zero_count % 2:
                result.append(num)
        else:
            result.append(num)
    return result
