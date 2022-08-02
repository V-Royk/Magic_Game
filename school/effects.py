class Effect:
    """
    Базовый класс для эффекта
    """

    def __init__(self, title, enemyDmg = 0, selfDmg = 0):
        self.title = title
        self.enemyDmg = enemyDmg
        self.selfDmg = selfDmg

class PureDamage(Effect):
    def __init__(self, enemyDmg):
        super().__init__("Чистый урон", enemyDmg)
    
    def execute(self, target, player):
        target.getDmg(self.enemyDmg)