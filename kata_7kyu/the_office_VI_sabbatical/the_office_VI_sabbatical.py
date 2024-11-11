def sabb(s, val, happiness):
    return "Sabbatical! Boom!" if val + happiness + sum(1 for char in s if char in "sabbatical") > 22 else "Back to your desk, boy."
