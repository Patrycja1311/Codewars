def get_free_urinals(urinals):
    if '11' in urinals: return -1
    urinals = list(urinals)
    return sum(urinals[i]=='0' and (i<1 or urinals[i-1]=='0') and (i+1==len(urinals) or urinals[i+1]=='0') and not urinals.__setitem__(i,'1') for i in range(len(urinals)))
