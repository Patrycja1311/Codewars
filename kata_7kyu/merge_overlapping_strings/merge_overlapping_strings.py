def merge_strings(first, second):
    for i in range(min(len(first), len(second)), -1, -1):
        if first.endswith(second[:i]):
            return first + second[i:]
