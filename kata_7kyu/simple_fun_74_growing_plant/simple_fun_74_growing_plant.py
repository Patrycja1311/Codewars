def growing_plant(up_speed, down_speed, desired_height):
    if desired_height <= 0:
        return 1
    days = 0
    height = 0
    while height < desired_height:
        days += 1
        height += up_speed
        if height >= desired_height:
            return days
        height -= down_speed
    return days
