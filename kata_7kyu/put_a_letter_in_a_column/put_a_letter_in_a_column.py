def build_row_text(index, character):
    cells = [' '] * 9
    cells[index] = character
    return '|' + '|'.join(cells) + '|'
