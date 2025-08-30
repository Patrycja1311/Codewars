def change_count(change):
    CHANGE = {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.10,
        "quarter": 0.25,
        "dollar": 1.00
    }
    total = sum(CHANGE[c] for c in change.split())
    return f"${total:.2f}"
