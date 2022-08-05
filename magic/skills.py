from .effects import PureDamage, Bleeding


class Skill:
    """
    Базовый класс для скилла
    """
    def __init__(self, title, effects = []):
        self.title = title
        self.effects = effects
    
    def execute(self, target, player):
        for effect in self.effects:
            effect.execute(target, player)

    def __str__(self):
        return f"Скилл '{self.title}'"

baseHit = Skill("Базовый удар", [PureDamage(10)])
cutHit  = Skill("Рубящий удар", [PureDamage(10), Bleeding(0.1)])
stabbingBlow = Skill('Колющий удар', [PureDamage(5), Bleeding(0.2)])
fencing = [baseHit, cutHit, stabbingBlow]