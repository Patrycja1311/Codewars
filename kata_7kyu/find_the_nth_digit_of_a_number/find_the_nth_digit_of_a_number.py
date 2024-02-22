def find_digit(num, nth):
    return -1 if nth <= 0 else int(str(abs(num))[-nth] if nth <= len(str(abs(num))) else 0)
