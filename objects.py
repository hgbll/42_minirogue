from random import randint

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
	def __init__(self, x, y, value):
		Item.__init__(self, x, y)
		self.value = value
		self.sym = "]"
		self.description = "a piece of leather"