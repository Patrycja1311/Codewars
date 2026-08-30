def apparently(st):
    words = st.split()
    return ' '.join(word + (' apparently' if word in ('and', 'but') and (i + 1 == len(words) or words[i + 1] != 'apparently') else '') for i, word in enumerate(words))
