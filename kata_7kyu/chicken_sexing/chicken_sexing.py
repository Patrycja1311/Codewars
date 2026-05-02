def correctness(bobs_decisions, expert_decisions):
    return sum(
        1 if b == e else 0.5 if '?' in (b, e) else 0
        for b, e in zip(bobs_decisions, expert_decisions)
    )
