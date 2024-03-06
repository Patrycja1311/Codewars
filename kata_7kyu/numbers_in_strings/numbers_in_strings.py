import re


def solve(s: str) -> int:
    numbers = re.findall(r'\d+', s)
    max_number = max(map(int, numbers))
    unique_string = ''.join(sorted(set(s), key=s.index))
    return max_number
