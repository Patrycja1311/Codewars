def get_rectangle_string(width, height):
    return (
        '*' * width + '\r\n' +
        ('*' + ' ' * (width - 2) + '*\r\n') * (height - 2) +
        '*' * width + '\r\n'
    ) if height > 1 else '*' * width + '\r\n'
