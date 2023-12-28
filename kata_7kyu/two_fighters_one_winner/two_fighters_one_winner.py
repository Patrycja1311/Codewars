def declare_winner(fighter1, fighter2, first_attacker):
    while all(f.health > 0 for f in (fighter1, fighter2)):
        attacker, defender = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
        defender.health -= attacker.damage_per_attack
        first_attacker = defender.name

    return fighter1.name if fighter1.health > 0 else fighter2.name
