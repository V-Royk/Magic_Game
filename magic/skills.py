from .effects import PureDamage, Bleeding, Burn, MagicDamage, Recovery, Critical
from .mobs import Player

class Skill:
    """
    Базовый класс для скилла
    """
    def __init__(self, title, effects = []):
        self.title = title
        self.effects = effects
    
    def execute(self, target:Player, player):
        for effect in self.effects:
            target.addEffect(effect)

    def __str__(self):
        return f"Скилл '{self.title}'"

baseHit = Skill("Базовый удар", [PureDamage(10)])
cutHit  = Skill("Рубящий удар", [PureDamage(10), Bleeding(0.1)])
stabbingBlow = Skill('Колющий удар', [PureDamage(5), Bleeding(0.2)])
fencing = [baseHit, cutHit, stabbingBlow]


pillarFire = Skill("Огненный столб", [MagicDamage(10), Burn(1, 5)])
fireWhip = Skill("Огненный кнут", [MagicDamage(10), Burn(1, 5)])
Fireball = Skill("Огненный шар", [MagicDamage(15), Burn(1, 5)])
fire = [pillarFire, fireWhip , stabbingBlow]


wave = Skill("Волна", [MagicDamage(7), Recovery(12)])
waterBubble  = Skill("Водянной пузырь", [MagicDamage(5), Recovery(20)])
jet = Skill('Струя', [MagicDamage(5), Recovery(15) ])
water = [wave, waterBubble, jet]


disarming = Skill("Обезоруживание", [Critical(3, 25, 50)])
high_kick = Skill("Высокий пинок", [Critical(4, 25, 50)])
jab = Skill('Прямой удар', [Critical(5, 25, 50)])
martialArts= [disarming, high_kick, jab]


# lightningDischarge = Skill("Разряд молний", [MagicDamage(1)])
# thunderclap = Skill("Раскат грома", [MagicDamage(2)])
# lightningBolt = Skill('Стрела молний', [MagicDamage(3)])
# lightning= [lightningDischarge,thunderclap, lightningBolt]


# stun = Skill("Оглушение",[MagicDamage(5)])
# fault = Skill("Разлом", [MagicDamage(5)])
# shaftOFstones= Skill('Вал из камней', [MagicDamage(5)])
# earth = [stun, fault, shaftOFstones]