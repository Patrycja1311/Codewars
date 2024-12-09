def transpose_two_strings(arr):
    max_length = max(len(arr[0]), len(arr[1]))
    return "\n".join(f"{arr[0].ljust(max_length)[i]} {arr[1].ljust(max_length)[i]}" for i in range(max_length))
