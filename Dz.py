class HealthPoint:
    name = 'HP'
    number = '100'
    HpS = '1:2' #HpS = соотношение здоровья к броне

    def __init__(self):
        print('OK')

pl1 = HealthPoint()
print(pl1.name)
print(pl1.number)
print(pl1.HpS)

pl2 = HealthPoint()
print(pl2.name)
print(pl2.number)
print(pl2.HpS)

print(HealthPoint.name)
print(HealthPoint.number)
print(HealthPoint.HpS)

class Shield:
    statname = 'SD'
    statnumber = '200'
    SpH = '2:1'

    def __init__(self):
        print('OK')


pl3 = Shield()
print(pl3.statname)
print(pl3.statnumber)
print(pl3.SpH)

pl4 = Shield()
print(pl4.statname)
print(pl4.statnumber)
print(pl4.SpH)

print(Shield.statname)
print(Shield.statnumber)
print(Shield.SpH)

class Experience:
    namestat = 'EXP'
    numberstat = '100'
    LvL = '20'

    def __init__(self):
        print('OK')


pl5 = Experience()
print(pl5.namestat)
print(pl5.numberstat)
print(pl5.LvL)

pl6 = Experience()
print(pl6.namestat)
print(pl6.numberstat)
print(pl6.LvL)

print(Experience.namestat)
print(Experience.numberstat)
print(Experience.LvL)