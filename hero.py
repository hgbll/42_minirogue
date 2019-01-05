from random import randint

class Hero:
    def __init__(self,x,y,lvl):
       self.hp = 12 + (lvl * 2)
       self.max_hp = 12 + (lvl * 2)
       self.str = 12 + lvl
       self.armor = 0
       self.x = x
       self.y = y
       self.xp = 0
       self.lvl = lvl
       self.hunger = 500
       self.accuracy = 5 + lvl
       self.defense = 10 + lvl/2
       self.damage = 0
       self.combat_status = ""
    
    def attack(self,enemy):
        if ((randint(0,20) + self.accuracy) > enemy.defense):
            self.damage = self.str - enemy.armor
            if (self.damage < 0):
                self.damage = 1
            enemy.hp -= self.damage
            self.combat_status = "you hit " + enemy.name + " [" + str(self.damage) + " damage(s)]"
        else:
            self.combat_status = "you miss " + enemy.name
enemy_list = [
    { "name": "Bat", "hp": 10, "str":8,"armor":0,"symbol": "B","acc": 4,"def": 8 },
    { "name": "Snake", "hp": 10, "str":11,"armor":0,"symbol": "S","acc": 6,"def": 7 },
    { "name": "Gobelin", "hp": 12, "str":8,"armor":0,"symbol": "G","acc": 5,"def": 9 },
    { "name": "Hobgobelin", "hp": 14, "str":14,"armor":1,"symbol": "H","acc": 5,"def": 11 },
]

class Enemy:
    def __init__(self,x,y,lvl,index):
       self.name= enemy_list[index]["name"]
       self.hp = enemy_list[index]["hp"] + (lvl * 2)
       self.str = enemy_list[index]["str"]+ lvl
       self.armor = enemy_list[index]["armor"]
       self.x = x
       self.y = y
       self.symbol = enemy_list[index]["symbol"]
       self.lvl = lvl
       self.accuracy = enemy_list[index]["acc"] + lvl
       self.defense = enemy_list[index]["def"] + lvl/2
       self.combat_status = ""
    
    def attack(self,enemy):
        if ((randint(0,20) + self.accuracy) > enemy.defense):
            self.damage = self.str - enemy.armor
            if (self.damage < 0):
                self.damage = 1
            enemy.hp -= self.damage
            self.combat_status = self.name + " hit you" + " [" + str(self.damage) + " damage(s)]"
        else:
            self.combat_status =  self.name + " miss you"


p1 = Hero(0,0,2)
p2 = Enemy(0,0,1,1)


"""
print(p2.name)
print(p2.defense)

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