class Player:

    alive = True
    effects = []

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


    def addEffect(self, effect):
        self.effects.append(effect)
        print(f"{self.name} получил эффект {effect.title}")
    

    def executeEffects(self):
        for i, effect in enumerate(self.effects):
            effect.execute(self)
            if effect.decreaseDuration():
                self.effects.pop(i)
                print(f"У {self.name} пропал эффект '{effect.title}'")

    
    def cast(self, i, enemy):
        skill = self.skills[i - 1]
        skill.execute(enemy, self)

        