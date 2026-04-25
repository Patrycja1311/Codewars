def dropzone(fire, dropzones):
    fx, fy = fire
    best = dropzones[0]
    best_dist = (best[0] - fx) ** 2 + (best[1] - fy) ** 2
    for d in dropzones[1:]:
        dist = (d[0] - fx) ** 2 + (d[1] - fy) ** 2
        if dist < best_dist:
            best = d
            best_dist = dist
    return best

