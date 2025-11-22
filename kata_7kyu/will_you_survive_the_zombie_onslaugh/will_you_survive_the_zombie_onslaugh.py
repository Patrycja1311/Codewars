def zombie_shootout(zombies, distance, ammo):
    killed = 0
    while zombies:
        if distance <= 0:
            return f"You shot {killed} zombies before being eaten: overwhelmed."
        if ammo == 0:
            return f"You shot {killed} zombies before being eaten: ran out of ammo."
        zombies -= 1; ammo -= 1; killed += 1
        distance -= 0.5
    return f"You shot all {killed} zombies."
