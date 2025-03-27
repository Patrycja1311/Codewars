def score_test(tests, right, omit, wrong):
    return sum(right if x == 0 else omit if x == 1 else -wrong for x in tests)
