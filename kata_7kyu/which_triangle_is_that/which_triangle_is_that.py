def type_of_triangle(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "Not a valid triangle"
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
