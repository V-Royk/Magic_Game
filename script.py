import magic.mobs as mobs
import magic.skills as skills
import magic.schools as schools

from random import randint

name = input("Введите имя героя: ")

pl = mobs.Player(name, 100)
en = mobs.Player("Враг(а)", 100)

available_schools = [schools.fencing, schools.water, schools.fire]

# pl.addSkill(schools.fencing.randomSkill())
# en.addSkill(schools.fencing.randomSkill())
# pl.addSkill(schools.water.skills[1])
# en.addSkill(schools.fire.randomSkill())
# pl.addSkill(schools.water.randomSkill())
# en.addSkill(schools.water.randomSkill())

while pl.alive and en.alive:
    school_index = int(input((
        "1 - фехтование\n"
        "2 - вода\n"
        "3 - огонь\n"
        "Введите, какую школу вы хотите освоить:"
        )))
    pl.addSkill(available_schools[school_index - 1].randomSkill())

    school_index = randint(1, 3)
    en.addSkill(available_schools[school_index - 1].randomSkill())

    print(pl)
    print(en)

    q = ""
    for i, skill in enumerate(pl.skills):
        q += f"{i + 1} - {skill.title}\n"
    skill_index = int(input(q + "Введите скилл для использования"))
    pl.cast(skill_index, en)

    skill_index = randint(1, len(en.skills))
    en.cast(skill_index, pl)
