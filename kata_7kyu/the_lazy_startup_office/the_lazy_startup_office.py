def bin_rota(arr):
    rota = []
    for i, row in enumerate(arr):
        rota.extend(row if i % 2 == 0 else row[::-1])
    return rota
