def i_tri(s):
    total = 140.6
    remaining = round(total - round(s, 2), 2)

    if s == 0:
        return 'Starting Line... Good Luck!'
    if remaining <= 0:
        return "You're done! Stop running!"
    if s < 2.4:
        return {'Swim': f'{remaining:.2f} to go!'}
    if s < 114.4:
        return {'Bike': f'{remaining:.2f} to go!'}
    return {'Run': 'Nearly there!' if remaining <= 10 else f'{remaining:.2f} to go!'}
