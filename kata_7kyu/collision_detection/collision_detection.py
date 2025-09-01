def collision(x1, y1, radius1, x2, y2, radius2):
    return (x2-x1)**2 + (y2-y1)**2 <= (radius1+radius2)**2
