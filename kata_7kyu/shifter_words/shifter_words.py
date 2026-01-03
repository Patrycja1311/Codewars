def shifter(st):
    ok = set("HINOSXZMW")
    return sum(1 for w in set(st.split()) if set(w) <= ok)
