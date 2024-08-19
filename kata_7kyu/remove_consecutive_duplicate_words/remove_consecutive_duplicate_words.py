import re


def remove_consecutive_duplicates(s: str) -> str:
    return re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', s)
