def drop_while(arr, pred):
    return next((arr[i:] for i, x in enumerate(arr) if not pred(x)), [])
