from .schools import fencing


class Player:

    alive = True

    def __init__(self, name, maxHP, skills = []):
        self.name = name
        self.hp = self.maxHP = maxHP
        self.skills = skills
        print(f"{name} появился на поле боя!")

    def getDmg(self, dmg):
        if self.hp - dmg > 0:
            print(f"{self.name} hp = {self.hp} - {dmg}/{self.maxHP}")
            self.hp -= dmg
        else:
            self.hp = 0
            self.alive = False
            print(f"{self.name} умер...")

    def addSkill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} получил скилл '{skill.title}'")
        