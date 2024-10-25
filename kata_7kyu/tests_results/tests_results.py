def test(r):
    avg = round(sum(r) / len(r), 3)
    counts = {'h': sum(1 for m in r if m >= 9),
              'a': sum(1 for m in r if 7 <= m <= 8),
              'l': sum(1 for m in r if m <= 6)}
    return [avg, counts, "They did well"] if counts['a'] == 0 and counts['l'] == 0 else [avg, counts]
