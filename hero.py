from random import randint
import actions_function
class Hero:
    def __init__(self,x,y,lvl):
       self.hp = 12 + (lvl * 2)
       self.str = (12 + lvl) / 2
       self.max_hp = 12 + (lvl * 2)
       self.max_str = (12 + lvl) / 2
       self.armor = 0
       self.x = x
       self.y = y
       self.xp = 0
       self.lvl = lvl
       self.hunger = 200
       self.accuracy = 5 + lvl
       self.defense = 10 + lvl/2
       self.damage = 0
       self.combat_status = ""
       self.inventory = []
       self.weak = False
       self.weapon = 0
    
    def attack(self,enemy):
        if ((randint(0,20) + self.accuracy) > enemy.defense):
            self.damage = self.str - enemy.armor
            if (self.damage < 0):
                self.damage = 1
            enemy.hp -= self.damage
            self.combat_status = "you hit " + enemy.name + " [" + str(self.damage) + " damage(s)]"
        else:
            self.combat_status = "you miss " + enemy.name
        if (enemy.hp <= 0):
            self.combat_status += " | Defeate " + enemy.name
enemy_list = [
    { "name": "Bat", "hp": 16, "str":8,"armor":0,"symbol": "B","acc": 4,"def": 8 },
    { "name": "Snake", "hp": 16, "str":11,"armor":1,"symbol": "S","acc": 6,"def": 7 },
    { "name": "Gobelin", "hp": 16, "str":8,"armor":2,"symbol": "G","acc": 5,"def": 9 },
    { "name": "Hobgobelin", "hp": 16, "str":14,"armor":2,"symbol": "H","acc": 5,"def": 11 },
]

class Enemy:
    def __init__(self,x,y,lvl,index):
       self.name= enemy_list[index]["name"]
       self.hp = enemy_list[index]["hp"] + (lvl * 2)
       self.str = (enemy_list[index]["str"]+ lvl) / 2
       self.armor = enemy_list[index]["armor"]
       self.x = x
       self.y = y
       self.symbol = enemy_list[index]["symbol"]
       self.lvl = lvl
       self.accuracy = enemy_list[index]["acc"] + lvl
       self.defense = enemy_list[index]["def"] + lvl/2
       self.combat_status = ""
       self.pursuit = False
       self.mouvement = 1
    
    def attack(self,hero):
        if ((randint(0,20) + self.accuracy) > hero.defense):
            self.damage = self.str - hero.armor
            if (self.damage < 0):
                self.damage = 1
            hero.hp -= self.damage
            self.combat_status = self.name + " hit you" + " [" + str(self.damage) + " damage(s)]"
        else:
            self.combat_status =  self.name + " miss you"
    
    def pursuit(self,hero):
        if(actions_function.get_distance(self,hero) > 10):
            self.pursuit = True

    def move(self,hero):
        if (self.x > hero.x + 1):
            self.x = self.x - self.mouvement;
        elif (self.x < hero.x - 1):
            self.x = self.x + self.mouvement;
        if (self.y > hero.y + 1):
            self.y = self.y - self.mouvement;
        elif (self.y < hero.y - 1):
            self.y = self.y + self.mouvement;
        
"""

p1 = Hero(0,30,2)
p2 = Enemy(0,0,1,3)


while (p1.x != p2.x or p1.y != p2.y):
    p2.move(p1)
    print("p2 x :"+ str(p2.x))
    print("p2 y :"+ str(p2.y))
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
"""
