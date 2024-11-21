def well(arr):
    good_count = sum(str(item).lower() == 'good' for sublist in arr for item in sublist)
    return 'Fail!' if good_count == 0 else 'Publish!' if good_count <= 2 else 'I smell a series!'
