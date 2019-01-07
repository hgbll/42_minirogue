from random import randint
import create_level


food_list = [
	"A mushroom",
	"A couple of nuts",
	"A rotten apple",
	"A moldy sandwich",
	"An egg"
]

armor_list = [
    { "name": "A piece of leather", "value": 1},
    { "name": "A well-made leather suit", "value": 2},
    { "name": "Some metal scraps", "value": 3},
    { "name": "A chainmail armor full of holes", "value": 5},
    { "name": "A crumbling plate armor", "value": 7},
    { "name": "A full body bronze suit", "value": 9}
]

weapon_list = [
    { "name": "A piece of stone", "value": 1},
    { "name": "A wooden sword", "value": 2},
    { "name": "A couple of throwing knives", "value": 3},
    { "name": "A rusty axe", "value": 5},
    { "name": "A balanced katana", "value": 8},
    { "name": "A holy greatsword", "value": 10},
]

potion_list = [
    { "name": "A simple red potion", "value": 1},
    { "name": "A magic potion", "value": 2},
    { "name": "A transparent potion", "value": 3},
    { "name": "A lava's potion", "value": 4},
    { "name": "A nice beer", "value": 5}, 
]


scroll_list = [
    { "name": "A piece of worthless paper", "value": 0},
    { "name": "A map", "value": 1},
    { "name": "A survival book", "value": 2},
    { "name": "An ancient text about stone circles", "value": 3}
]

class Item:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.sym = ""

class Treasure(Item):
	def __init__(self, x, y):
		Item.__init__(self, x, y)
		self.value = randint(20, 100)
		self.sym = "*"

class Food(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.sym = ":"
		self.description = food_list[min(index, len(food_list) - 1)]


class Armor(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = armor_list[min(index, len(armor_list) - 1)]["value"]
		self.sym = "]"
		self.description = armor_list[min(index, len(armor_list) - 1)]["name"]

class Weapon(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = weapon_list[min(index, len(weapon_list) - 1)]["value"]
		self.sym = ")"
		self.description = weapon_list[min(index, len(weapon_list) - 1)]["name"]

class Potion(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = potion_list[min(index, len(potion_list) - 1)]["value"]
		self.sym = "!"
		self.description = potion_list[min(index, len(potion_list) - 1)]["name"]

	def take_potion(self, game):
		if self.value == 1:
			game.hero.hp = min(game.hero.hp + 5 + 2* game.hero.lvl, game.hero.max_hp)
		elif self.value == 2:
			game.hero.xp = game.hero.next_lvl
		elif self.value == 3:
			game.hero.view_distance += 1
		elif self.value == 4:
			game.hero.defense += 3
		elif self.value == 5:
			game.hero.hp = game.hero.max_hp
			game.hero.view_distance -= 1
class Scroll(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = scroll_list[min(index, len(scroll_list) - 1)]["value"]
		self.sym = "?"
		self.description = scroll_list[min(index, len(scroll_list) - 1)]["name"]

	def read_scroll(self, game):
		if self.value == 0:
			game.title = "Nothing happens"
		elif self.value == 1:
			game.hidden = [[False] * 80 for i in range(22)]
			game.title = "Suddenly you can see"
		elif self.value == 2:
			game.hero.max_hunger += 100
			game.title = "I feel already less hungry"
		elif self.value == 3:
			create_level.create_level(game)
			game.title = "Finally, next level!"

item_types = [Armor, Weapon, Potion, Scroll]
