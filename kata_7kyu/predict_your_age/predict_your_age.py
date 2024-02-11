import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    result = sum(age * age for age in ages)
    result = math.sqrt(result) / 2
    return math.floor(result)
