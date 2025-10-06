def quicksum(packet):
    if not packet or not packet[0].isalpha() or not packet[-1].isalpha() or any(c != ' ' and not ('A' <= c <= 'Z') for c in packet):
        return 0
    return sum((i+1) * (ord(c)-64 if c != ' ' else 0) for i, c in enumerate(packet))
