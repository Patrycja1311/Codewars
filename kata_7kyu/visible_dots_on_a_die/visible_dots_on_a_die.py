def total_amount_visible(top_num, num_of_sides):
    opposite_sum = (num_of_sides + 1) - top_num
    total_dots = (num_of_sides * (num_of_sides + 1)) // 2
    visible_dots = total_dots - opposite_sum
    return visible_dots
