import random as rd


herohp = rd.randrange(50,100)
monsterhp = rd.randrange(50,100)
stack = 0;
print("hero HP :", herohp ,"monster HP :",monsterhp)
win = ("succes")
lose = ("fail")
while herohp >= 0 and monsterhp >= 0:
  heroatt = rd.randrange(-10,20)
  monsteratt = rd.randrange(-10,20)
  if heroatt > 0:
    if monsteratt > 0:
      herohp = herohp - monsteratt
      monsterhp = monsterhp - heroatt
      print("hero(HP:", herohp ,", attack:", heroatt ,")", win," <-> monster(HP:",monsterhp,"), attack:",monsteratt,")",win)
    elif monsteratt < 0:
      monsterhp = monsterhp - heroatt
      print("hero(HP:", herohp ,", attack:", heroatt ,")", win," <-> monster(HP:",monsterhp,"), attack:",monsteratt,")",lose)
  
  if heroatt < 0:
    if monsteratt > 0:
      herohp = herohp - monsteratt
      print("hero(HP:", herohp ,", attack:", heroatt ,")", lose," <-> monster(HP:",monsterhp,"), attack:",monsteratt,")",win)
    else:
      print("hero(HP:", herohp ,", attack:", heroatt ,")", lose," <-> monster(HP:",monsterhp,"), attack:",monsteratt,")",lose)
  stack += 1
  if(herohp<0):
    judge = ("Monster Win!!!!")
  else:
    judge = ("Hero Win!!!!")
print("---------------------------------------------------------")
print("Total phase:",stack)
print(judge)
