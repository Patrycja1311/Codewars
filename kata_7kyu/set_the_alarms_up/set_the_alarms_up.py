def set_the_alarms_up(time, n):
    h, m = map(int, time.split(":"))
    return [f"{(h + (m + 5*i)//60)%24:02d}:{(m + 5*i)%60:02d}" for i in range(n)]
