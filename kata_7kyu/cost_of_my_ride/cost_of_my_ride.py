def insurance(age, size, num_of_days):
    if num_of_days <= 0:
        return 0
    daily_cost = 50 + (10 if age < 25 else 0) + {"economy": 0, "medium": 10, "full-size": 15}.get(size, 15)
    return daily_cost * num_of_days
