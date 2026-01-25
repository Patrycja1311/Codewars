def goto(level,button):
    if not isinstance(level, int) or level not in range(4):
        return 0
    if not isinstance(button, str) or button not in '0123':
        return 0
    return int(button) - level
