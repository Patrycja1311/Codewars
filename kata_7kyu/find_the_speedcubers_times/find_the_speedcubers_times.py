def cube_times(times):
    fastest = min(times)
    times.remove(fastest)
    times.remove(max(times))
    average = round(sum(times) / 3, 2)
    return (average, fastest)
