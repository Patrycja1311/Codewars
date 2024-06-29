def find_screen_height(width, ratio):
    w_ratio, h_ratio = map(int, ratio.split(':'))
    return f"{width}x{(width * h_ratio) // w_ratio}"
