def can_i_play(now_hour, start_hour, end_hour):
    if start_hour <= end_hour:
        return start_hour <= now_hour < end_hour
    else:
        return now_hour >= start_hour or now_hour < end_hour
