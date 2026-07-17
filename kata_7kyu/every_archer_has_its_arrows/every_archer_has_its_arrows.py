def archers_ready(archers):
    return bool(archers) and all(a >= 5 for a in archers)
