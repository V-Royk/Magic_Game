class Effect:
    """
    Базовый класс для эффекта
    """

    def __init__(self, title, enemyDmg = 0, selfDmg = 0):
        self.title = title
        self.enemyDmg = enemyDmg
        self.selfDmg = selfDmg

class Bleeding(Effect):
    def __init__(self, procent):
        super().__init__("Кровотечение")
        self.procent = procent

    def execute(self, target, player):
        target.getDmg(target.hp * self.procent)

class PureDamage(Effect):
    def __init__(self, dmg):
        super().__init__("Чистый урон", dmg)
    
    def execute(self, target, player):
        target.getDmg(self.enemyDmg)