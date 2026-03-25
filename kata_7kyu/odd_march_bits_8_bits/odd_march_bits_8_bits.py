def bit_march(n: int) -> list:
    return [[int(c) for c in f'{((1<<n)-1)<<i:08b}'] for i in range(8-n+1)]
