from .effects import PureDamage
class Skill:
    """
    Базовый класс для скилла
    """
    def __init__(self, title, effects):
        self.title = title
        self.effects = effects
    
    def execute(self, target, player):
        for effect in self.effects:
            effect.execute(target, player)

baseHit = Skill("Базовый удар", [PureDamage(10)])