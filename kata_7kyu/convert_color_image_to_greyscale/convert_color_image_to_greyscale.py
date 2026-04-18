def color_2_grey(image):
    return [
        [[(avg := round((r+g+b)/3))]*3 for r, g, b in row]
        for row in image
    ]
