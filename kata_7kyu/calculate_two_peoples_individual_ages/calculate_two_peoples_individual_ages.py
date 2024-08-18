def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return None
    age1 = (sum_+difference)/2
    age2 = (sum_-difference)/2
    return (age1,age2) if age1>=0 and age2>=0 else None
