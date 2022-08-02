class Player:

    alive = True

    def __init__(self, name, maxHP):
        self.name = name
        self.hp = self.maxHP = maxHP

    def getDmg(self, dmg):
        if self.hp - dmg > 0:
            print(f"{self.name} hp = {self.hp} - {dmg}/{self.maxHP}")
            self.hp -= dmg
        else:
            self.hp = 0
            self.alive = False
            print(f"{self.name} умер...")
        