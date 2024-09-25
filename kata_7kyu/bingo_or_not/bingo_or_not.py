def bingo(array):
    return "WIN" if {'B', 'I', 'N', 'G', 'O'}.issubset({chr(64 + num) for num in array}) else "LOSE"
