def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' not in arrow or not arrow['damaged']:
            return True
    return False
