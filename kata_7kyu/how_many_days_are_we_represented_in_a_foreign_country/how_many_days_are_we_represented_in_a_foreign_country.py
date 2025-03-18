def days_represented(trips):
    return len({d for start, end in trips for d in range(start, end + 1)})
