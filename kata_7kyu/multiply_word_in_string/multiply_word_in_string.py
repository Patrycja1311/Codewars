def modify_multiply(st, loc, num):
    words = st.split()
    word = words[loc]
    result = "-".join([word] * num)
    return result
