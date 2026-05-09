def euclidean_distance(point1: list[int], point2: list[int]) -> float:
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

