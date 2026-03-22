def yoga(classroom, poses):
    total = 0
    for row in classroom:
        row_sum = sum(row)
        for person in row:
            for pose in poses:
                if row_sum + person >= pose:
                    total += 1
    return total
