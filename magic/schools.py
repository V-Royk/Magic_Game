from random import randint
from .skills import fencing


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