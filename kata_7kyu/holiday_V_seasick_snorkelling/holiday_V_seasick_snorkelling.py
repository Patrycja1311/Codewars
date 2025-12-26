def sea_sick(sea):
    return "Throw Up" if sum(sea[i] != sea[i-1] for i in range(1,len(sea))) > 0.2*len(sea) else "No Problem"
