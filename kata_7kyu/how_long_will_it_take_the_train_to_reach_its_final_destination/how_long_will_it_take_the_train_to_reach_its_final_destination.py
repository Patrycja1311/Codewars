def reach_destination(distance, speed):
    t = round(distance / speed * 2) / 2
    t_str = str(int(t)) if t.is_integer() else str(t)
    return f"The train will be there in {t_str} hour{'s' * (t != 1)}."
