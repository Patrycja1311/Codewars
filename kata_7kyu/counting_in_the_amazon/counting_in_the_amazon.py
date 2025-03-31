def count_arara(n):
    adak_count = n // 2
    anane_count = n % 2

    result = ["adak"] * adak_count + (["anane"] if anane_count else [])

    return " ".join(result)
