def candies(lst):
    if len(lst) <= 1:
        return -1
    max_candies = max(lst)
    total_candies_given = sum(max_candies - candy for candy in lst)
    return total_candies_given
