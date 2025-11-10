def remove(st):
    return " ".join(w.rstrip("!") for w in st.split())
