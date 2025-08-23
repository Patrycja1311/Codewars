def decode_resistor_colors(bands):
    c={"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9}
    t={"gold": "5%", "silver": "10%"}
    b=bands.split()
    ohms=(10*c[b[0]]+c[b[1]])*10**c[b[2]]
    tol=t.get(b[3], "20%") if len(b)>3 else "20%"
    return (f"{ohms} ohms, {tol}" if ohms<1000 else
            f"{ohms/1000:.{0 if ohms%1000==0 else 1}f}k ohms, {tol}" if ohms<1_000_000 else
            f"{ohms/1_000_000:.{0 if ohms%1_000_000==0 else 1}f}M ohms, {tol}")
