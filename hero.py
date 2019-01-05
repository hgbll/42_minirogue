from random import randint

class Hero:
    def __init__(self,x,y,lvl):
       self.hp = 12 + (lvl * 2)
       self.max_hp = 12 + (lvl * 2)
       self.str = 12 + lvl
       seff.armor = 0
       self.x = x
       self.y = y
       self.xp = 0
       self.lvl = lvl
       self.accuracy = 5 + lvl
       self.defense = 10 + lvl
       self.combat_status = ""
    
    def attack(self,enemy)
        if ((randint(0,20) + self.accuracy) > enemy.defense)
            self.combat_status = "you hit"
			enemy.hp -= self.str
        else
            self.combat_status = "you miss"