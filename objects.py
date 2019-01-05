from random import randint

armor_list = [
    { "name": "a piece of leather", "value": 1},
    { "name": "a well-made leather suit", "value": 2},
    { "name": "some metal scraps", "value": 3},
    { "name": "a rusty plate armor", "value": 6},
]

weapon_list = [
    { "name": "a piece of stone", "value": 1},
    { "name": "a wodden sword", "value": 2},
    { "name": "a couple of arrows", "value": 3},
    { "name": "a crumbling axe", "value": 6},
]

potion_list = [
    { "name": "a simple red potion", "value": 1},
    { "name": "a magic potion", "value": 2},
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
	def __init__(self, x, y):
		Item.__init__(self, x, y)
		self.sym = ":"
		self.description = "some food"

class Armor(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = armor_list[index]["value"]
		self.sym = "]"
		self.description = armor_list[index]["name"]

class Weapon(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = weapon_list[index]["value"]
		self.sym = ")"
		self.description = weapon_list[index]["name"]

class Potion(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = weapon_list[index]["value"]
		self.sym = ")"
		self.description = weapon_list[index]["name"]