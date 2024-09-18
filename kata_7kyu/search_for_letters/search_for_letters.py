def change(st):
    return ''.join('1' if chr(i) in st.lower() else '0' for i in range(97, 123))
