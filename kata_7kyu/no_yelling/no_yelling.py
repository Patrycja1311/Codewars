def filter_words(st):
    cleaned = " ".join(st.split())
    cleaned = cleaned.lower()
    return cleaned.capitalize()
