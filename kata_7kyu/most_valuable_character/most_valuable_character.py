def solve(st):
    max_value = -1
    best_char = ''
    for char in set(st):
        first = st.find(char)
        last = st.rfind(char)
        value = last - first
        if value > max_value or (value == max_value and char < best_char):
            max_value = value
            best_char = char
    return best_char
