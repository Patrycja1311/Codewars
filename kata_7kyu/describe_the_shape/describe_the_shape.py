def describe_the_shape(angles):
    return "this will be a line segment or a dot" if angles <= 2 else f"This shape has {angles} sides and each angle measures {int((angles-2)*180/angles)}"
