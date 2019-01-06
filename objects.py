from random import randint

food_list = [
	"a mushroom",
	"a couple of nuts",
	"a rotten apple",
	"a moldy sandwich",
	"an egg"
]

armor_list = [
    { "name": "a piece of leather", "value": 1},
    { "name": "a well-made leather suit", "value": 2},
    { "name": "some metal scraps", "value": 3},
    { "name": "a rusty plate armor", "value": 6},
]

weapon_list = [
    { "name": "a piece of stone", "value": 1},
    { "name": "a wooden sword", "value": 2},
    { "name": "a couple of arrows", "value": 3},
    { "name": "a crumbling axe", "value": 6},
]

potion_list = [
    { "name": "a simple red potion", "value": 1},
    { "name": "a magic potion", "value": 2},
    { "name": "a transparent potion", "value": 3}
]

scroll_list = [
	{ "name": "a piece of worthless paper", "value": 0},
    { "name": "a map", "value": 1},
    { "name": "a survival book", "value": 2},
    { "name": "an ancient text about stone circles", "value": 3}
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
			game.hero.hp = min(game.hero.hp + 5, game.hero.max_hp)
		elif self.value == 2:
			game.hero.xp = game.hero.next_lvl
		elif self.value == 3:
			game.hero.view_distance += 1

class Scroll(Item):
	def __init__(self, x, y, index):
		Item.__init__(self, x, y)
		self.value = scroll_list[min(index, len(scroll_list) - 1)]["value"]
		self.sym = "?"
		self.description = scroll_list[min(index, len(scroll_list) - 1)]["name"]

	def read_scroll(self, game):
		if self.value == 0:
			game.title = "nothing happens"
		elif self.value == 1:
			game.hidden = [[False] * 80 for i in range(22)]
			game.title = "suddenly you can see"
		elif self.value == 2:
			game.hero.max_hunger += 100
			game.title = "i feel already less hungry"
		elif self.value == 3:
			game.hero.x, game.hero.y = filter(lambda x: x[0] != -1, [(line.find('%'), i) for i, line in enumerate(game.level)])[0]
			game.title = "finally, next level!"

item_types = [Armor, Weapon, Potion, Scroll]
