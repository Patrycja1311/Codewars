def binary_fingers(bin_string):
    fingers = ["Thumb", "Index", "Middle", "Ring", "Pinkie"]
    return [fingers[i] for i, b in enumerate(bin_string[::-1]) if b == "1"][::-1]
