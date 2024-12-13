class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, target, hits):
        target.health -= hits * 10
        if target.health < 0:
            target.health = 0
