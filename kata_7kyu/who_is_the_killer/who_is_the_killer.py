def killer(suspect_info, dead):
    return next((suspect for suspect, seen_people in suspect_info.items() if all(person in seen_people for person in dead)), None)
