import magic.mobs as mobs
import magic.skills as skills
import magic.schools as schools

name = input("Введите имя героя: ")

pl = mobs.Player(name, 100)
en = mobs.Player("Враг", 20)

pl.addSkill(schools.fencing.randomSkill())
en.addSkill(schools.fencing.randomSkill())