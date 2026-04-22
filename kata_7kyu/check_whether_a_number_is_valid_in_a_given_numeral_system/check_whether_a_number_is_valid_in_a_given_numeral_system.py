def validate_base(num: str, base: int) -> bool:
    return all(
        (int(c) if c.isdigit() else ord(c) - 55) < base
        for c in str(num)
    )
