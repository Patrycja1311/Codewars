def vowel_start(st):
    st=''.join(filter(str.isalnum,st.lower()))
    return ''.join(' '+c if c in'aeiou' else c for c in st).strip()
