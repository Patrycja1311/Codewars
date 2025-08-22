def cake(candles, debris):
    if not candles: return "That was close!"
    fallen = sum(ord(c) if i%2==0 else ord(c)-96 for i,c in enumerate(debris))
    return "Fire!" if fallen > candles*0.7 else "That was close!"
