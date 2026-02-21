def total_licks(env):
    total = 252 + sum(env.values())
    toughest = max(env.items(), key=lambda x: x[1])[0] if env and max(env.values()) > 0 else None

    result = f"It took {total} licks to get to the tootsie roll center of a tootsie pop."
    if toughest:
        result += f" The toughest challenge was {toughest}."
    return result
