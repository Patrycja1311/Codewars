def solve(st,k):
    for c in sorted(set(st)):
        st, k = st.replace(c, '', k), max(0, k - st.count(c))
        if k == 0:
            break
    return st
