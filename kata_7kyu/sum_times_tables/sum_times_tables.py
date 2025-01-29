def sum_times_tables(table, a, b):
    return sum(t * (b - a + 1) * (a + b) // 2 for t in table) if table and a <= b else 0
