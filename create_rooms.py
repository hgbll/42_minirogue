from random import randint

class Room:

    def __init__(self, zone):

        right_border = (zone % 3) * 26 + 26
        bottom_border = (zone / 3) * 7 + 7 + (1 if zone / 3 == 2 else 0)

        self.anchor_x = right_border - (6 + randint(0, 19))
        self.anchor_y = bottom_border - (5 + randint(0, 1) + (1 if zone / 3 == 2 else 0))

        bigger = 1 if randint(0, 100) <= 75 else 0
        self.width = randint(3 + bigger, 3 + bigger + (right_border - self.anchor_x - 6))
        self.height = randint(3 + bigger, 3 + bigger + (bottom_border - self.anchor_y - 5))

        self.zone = zone

        self.door_north = (0, 0) if zone / 3 == 0 else (randint(self.anchor_x + 1, self.anchor_x + self.width - 1), self.anchor_y)
        self.door_south = (0, 0) if zone / 3 == 2 else (randint(self.anchor_x + 1, self.anchor_x + self.width - 1), self.anchor_y + self.height)
        self.door_west = (0, 0) if zone % 3 == 0 else (self.anchor_x, randint(self.anchor_y + 1, self.anchor_y + self.height - 1))
        self.door_east = (0, 0) if zone % 3 == 2 else (self.anchor_x + self.width, randint(self.anchor_y + 1, self.anchor_y + self.height - 1))

        self.box = [
                {"min_x": self.anchor_x + 1, "max_x": self.anchor_x + self.width - 1, "min_y": self.anchor_y + 1, "max_y": self.anchor_y + self.height - 1},
        ]
   
def create_rooms():

    rooms = []
    for i in range(0, 9):
        rooms.append(Room(i))
    return (rooms)
