def countzero(st):
    return sum(st.count(x) for x in "abdegopq069DOPQR") + 2 * sum(st.count(x) for x in "%&B8") + st.count("()")
