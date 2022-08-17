from random import randint
from .skills import fencing
from .skills import fire
from .skills import water
from .skills import martialArts
# from .skills import earth 


class School:
    """
    Базовый класс школы
    """
    def __init__(self, title, skills = []):
        self.title = title
        self.skills = skills

    def randomSkill(self):
        i = randint(0, len(self.skills) - 1)
        return self.skills[i]

fencing = School("Фехтование", fencing)

fire = School("Огонь", fire)

water = School('Вода', water)

martialArts = School('Боевые искусства', martialArts)

# earth =  School('Земля', earth)

# lightning = School('Молния', lightning)