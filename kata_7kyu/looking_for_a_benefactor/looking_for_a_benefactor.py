import math


def new_avg(arr, newavg):
    next_donation = math.ceil(newavg * (len(arr) + 1) - sum(arr))
    if next_donation <= 0:
        raise ValueError("The next donation must be a positive value to reach the desired average.")
    return next_donation
