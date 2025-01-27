def process_array(arr, callback):
    return [callback(element) for element in arr]
