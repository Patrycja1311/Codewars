def negation_value(s: str, val) -> bool:
    return bool(val) if len(s) % 2 == 0 else not bool(val)
