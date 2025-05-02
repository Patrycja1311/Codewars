def solve(a, b):
    x = sum(i > j for i, j in zip(a, b))
    y = sum(i < j for i, j in zip(a, b))
    msg = ["Alice made \"Kurt\" proud!", "that looks like a \"draw\"! Rock on!", "Bob made \"Jeff\" proud!"]
    return f"{x}, {y}: {msg[1 if x == y else 0 if x > y else 2]}"
