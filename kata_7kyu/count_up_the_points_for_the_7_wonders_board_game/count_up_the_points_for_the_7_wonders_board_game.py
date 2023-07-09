def seven_wonders_science(compasses, gears, tablets):

    distinct_sets = min(compasses, gears, tablets)
    step1_score = distinct_sets * 7

    compass_score = compasses * compasses
    gear_score = gears * gears
    tablet_score = tablets * tablets
    step2_score = compass_score + gear_score + tablet_score

    final_score = step1_score + step2_score

    return final_score
