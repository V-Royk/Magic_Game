import magic.mobs as mobs
import magic.skills as skills
import magic.schools as schools

name = input("Введите имя героя: ")

pl = mobs.Player(name, 100)
en = mobs.Player("Враг", 100)

pl.addSkill(schools.fencing.randomSkill())
en.addSkill(schools.fencing.randomSkill())
pl.addSkill(schools.fire.skills[0])
en.addSkill(schools.fire.randomSkill())
pl.addSkill(schools.water.randomSkill())
en.addSkill(schools.water.randomSkill())

pl.cast(3, en)
en.executeEffects()
en.executeEffects()
en.executeEffects()
en.executeEffects()