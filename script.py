import school.mobs as mobs
import school.skills as skills

pl = mobs.Player("Игрок", 100)
en = mobs.Player("Враг", 20)

skills.baseHit.execute(en, pl)