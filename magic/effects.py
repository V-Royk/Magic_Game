from random import randint


class Effect:
    """
    Базовый класс для эффекта
    """

    def __init__(self, title, enemyDmg = 0, selfDmg = 0, healing = 0, duration = 1):
        self.title = title
        self.enemyDmg = enemyDmg
        self.selfDmg = selfDmg
        self.healing = healing
        self.duration = duration

    def decreaseDuration(self):
        self.duration -= 1
        return self.duration == 0

class Bleeding(Effect):
    def __init__(self, procent):
        super().__init__("Кровотечение")
        self.procent = procent

    def execute(self, target):
        target.getDmg(target.hp * self.procent)

class PureDamage(Effect):
    def __init__(self, dmg):
        super().__init__("Чистый урон", dmg)
    
    def execute(self, target):
        target.getDmg(self.enemyDmg)


class Burn(Effect):
    def __init__(self, start, end):
        dmg = randint(start, end)
        super().__init__("Горение", dmg, duration=3)

    def execute(self, target):
        target.getDmg(self.enemyDmg)


class MagicDamage(Effect):
    def __init__(self, dmg):
        super().__init__("Магический урон", dmg)
    
    def execute(self, target):
        target.getDmg(self.enemyDmg)


class Recovery(Effect):
    def __init__(self, healing):
        super().__init__("Восстановление", 0, -healing)

    def execute(self, target):
        target.getDmg(self.enemyDmg)


class Critical(Effect):
    def __init__(self, dmg, start, end):
        dmg = dmg + dmg * (randint(start, end)/100)
        super().__init__("Критический урон", dmg)
        

    def execute(self, target):
        target.getDmg(self.enemyDmg)


class Stun(Effect):
    def __init__(self, dmg):
        super().__init__("Оглушение", dmg, duration=1)


    def execute(self, target):
        target.getDmg(self.enemyDmg==0)

class oOverload(Effect):
    def __init__(self, dmg):
        super().__init__("Перегрузка", dmg)
        

    def execute(self, target):
        target.getDmg(self.enemyDmg * 2)