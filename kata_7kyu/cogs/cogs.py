def cog_RPM(cogs):
    rpm = 1 * (cogs[0] / cogs[-1])
    if len(cogs) % 2 == 0:
        return -rpm
    else:
        return rpm
