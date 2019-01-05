from random import randint

class Hero:
    def __init__(self,x,y,lvl):
       self.hp = 12 + (lvl * 2)
       self.str = 12 + lvl
       self.armor = 0
       self.x = x
       self.y = y
       self.xp = 0
       self.lvl = lvl
       self.accuracy = 5 + lvl
       self.defense = 10 + lvl/2
       self.combat_status = ""
    
    def attack(self,enemy):
        if ((randint(0,20) + self.accuracy) > enemy.defense):
            self.combat_status = "you hit"
            enemy.hp -= self.str
        else:
            self.combat_status = "you miss"

class Enemy:
    def __init__(self,x,y,lvl):
       self.name= ""
       self.hp = 12 + (lvl * 2)
       self.str = 12 + lvl
       self.armor = 0
       self.x = x
       self.y = y
       self.symbol = ""
       self.lvl = lvl
       self.accuracy = 5 + lvl
       self.defense = 10 + lvl/2
       self.combat_status = ""
    
    def attack(self,enemy):
        if ((randint(0,20) + self.accuracy) > enemy.defense):
            self.combat_status = "you hit"
            enemy.hp -= self.str
        else:
            self.combat_status = "you miss"

p1 = Hero(0,0,2)
p2 = Enemy(0,0,2)
while (p1.hp > 0 and p2.hp > 0):
    
    print(p1.hp)
    print(p2.hp)
    p1.attack(p2)
    print(p1.combat_status)
    print(p2.hp)
    p2.attack(p1)
    print(p2.combat_status)
    print(p1.hp)

print(p1.hp)
print(p2.hp)