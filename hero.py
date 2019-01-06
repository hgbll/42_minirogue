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
       self.next_lvl = 10
       self.hunger = 300
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
            self.combat_status = "you hit " + enemy.name + " [" + str(self.damage) + " damage]"
        else:
            self.combat_status = "you miss " + enemy.name
        if (enemy.hp <= 0):
            self.combat_status += " | Defeated " + enemy.name
    
    def levelup(self,game):
        if (self.xp >= self.next_lvl):
            self.max_hp += 3
            self.hp = self.max_hp
            self.max_str += 1
            self.str = self.max_str
            self.lvl += 1
            self.xp = self.xp - self.next_lvl
            self.next_lvl = 10 + (self.lvl * 2)
            game.title = "You are level " + str(self.lvl) +" !"

    def update(self, game):
        game.hero.hunger -= 1
        if game.hero.hunger < 100 and not game.hero.weak:
            if game.title != "":
                add_more(game)
            game.title = "you feel weak"
            game.hero.str /= 2
            game.hero.weak = True

        if self.hp <= 0 or game.hero.hunger <= 0:
            game.game_over = True 
        self.levelup(game)

    def get_room_index(self, game):
        for i, room in enumerate(game.rooms):
            if (self.x >= room.box['min_x'] and self.x <= room.box['max_x'] and self.y >= room.box['min_y'] and self.y <= room.box['max_y']):
                return i
        return -1

enemy_list = [
    { "name": "Bat", "hp": 10, "str":6,"armor":0,"symbol": "B","acc": 4,"def": 8 , "range" : 3, "exp": 8},
    { "name": "Snake", "hp": 10, "str":7,"armor":0,"symbol": "S","acc": 6,"def": 7,"range" : 4, "exp": 8 },
    { "name": "Gobelin", "hp": 10, "str":8,"armor":1,"symbol": "G","acc": 5,"def": 9,"range" : 3, "exp": 6 },
    { "name": "Hobgobelin", "hp": 16, "str":8,"armor":2,"symbol": "H","acc": 5,"def": 11,"range" : 3, "exp": 10 },
	{ "name": "Norminet", "hp": 24, "str":8,"armor":2,"symbol": "N","acc": 8,"def": 18,"range" : 0, "exp": 20 },
]
free_tiles = ['.', '#', '+', '%']

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
       self.pursuit_status = False
       self.mouvement = 1
       self.detection_range = enemy_list[index]["range"]
       self.can_attack = False
       self.triggered = False
       self.can_see_hero = False
       self.exp = enemy_list[index]["exp"] * lvl
    
    def attack(self,hero):
        if ((randint(0,20) + self.accuracy) > hero.defense):
            self.damage = self.str - hero.armor
            if (self.damage < 0):
                self.damage = 1
            hero.hp -= self.damage
            self.combat_status = self.name + " hit you" + " [" + str(self.damage) + " damage]"
        else:
            self.combat_status =  self.name + " miss you"
    
    def pursuit(self,hero):
        if (actions_function.get_distance(self,hero) < self.detection_range and self.can_see_hero == True) or self.triggered == True:
            self.pursuit_status = True

    def check_for_monster(self, game, next_x, next_y):
        if ((next_x != game.hero.x) != (next_y != game.hero.y)):
            for m in game.monsters:
                if m.y == next_y:
                    if m.x != next_x:
                       self.x = next_x
                       self.y = next_y
                       return(1)
                if m.x == next_x:
                    if m.y != next_y:
                       self.x = next_x
                       self.y = next_y
                       return(1)
        return(0) 


    def move(self,hero, level, game):
        if self.pursuit_status == True and actions_function.get_distance(self,hero) >= 1:
            if self.x > hero.x and level[self.y][self.x - self.mouvement] in free_tiles:
                self.check_for_monster(game, self.x - self.mouvement, self.y)
            elif self.x < hero.x and level[self.y][self.x + self.mouvement] in free_tiles:
                self.check_for_monster(game, self.x + self.mouvement, self.y)
            if self.y > hero.y and level[self.y - self.mouvement][self.x] in free_tiles:
                self.check_for_monster(game, self.x , self.y - self.mouvement)
            elif self.y < hero.y and level[self.y + self.mouvement][self.x] in free_tiles:
                self.check_for_monster(game, self.x , self.y + self.mouvement)


    def update(self, hero, game):
        self.hero_in_room(hero,game)
        if actions_function.get_distance(self,hero) < 2:
            self.can_attack = True
        else:
            self.can_attack = False
        self.pursuit(hero)
        self.move(hero, game.level, game)

    def get_room_index(self, game):
        for i, room in enumerate(game.rooms):
            if (self.x >= room.box['min_x'] and self.x <= room.box['max_x'] and self.y >= room.box['min_y'] and self.y <= room.box['max_y']):
                return i
        return -1

    def hero_in_room(self, hero, game):
        if self.get_room_index(game) == hero.get_room_index(game):
            self.can_see_hero = True 
        else:
            self.can_see_hero = False

