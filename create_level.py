from random import randint

"""
        self.anchor_x = right_border - (6 + randint(0, 20))
        self.anchor_y = bottom_border - (5 + randint(0, 2))

        self.width = randint(3, 3 + (right_border - self.anchor_x - 6))
        self.height = randint(3, 3 +  (bottom_border - self.anchor_y - 5))
"""
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

   
def get_char(i, j, k, rooms, level):
    
    if (j == rooms[i].anchor_y or j == rooms[i].anchor_y + rooms[i].height) and (k >= rooms[i].anchor_x and k <= rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '-'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k == rooms[i].anchor_x or k == rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '|'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k > rooms[i].anchor_x and k < rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '.'

    if (k != 0 and j != 0):
        if (j == rooms[i].door_north[1] and k == rooms[i].door_north[0]):
            level[j][k] = '+'
        if (j == rooms[i].door_west[1] and k == rooms[i].door_west[0]):
            level[j][k] = '+'
        if (j == rooms[i].door_south[1] and k == rooms[i].door_south[0]):
            level[j][k] = '+'
        if (j == rooms[i].door_east[1] and k == rooms[i].door_east[0]):
            level[j][k] = '+'

def create_rooms():

    rooms = []
    for i in range(0, 9):
        rooms.append(Room(i))
    return (rooms)

def put_corridor(level, door1, door2):

    if door1[0] == door2[0]:
        direction = 1 if door1[1] < door2[1] else -1
        for i in range(door1[1], door2[1]):
            print str(i)
            level[i * direction][door1[0]] = '#'

    if door1[1] == door2[1]:
        direction = 1 if door1[0] < door2[0] else -1
        for i in range(door1[0] + 1, door2[0]):
            print str(i)
            level[i * direction][door1[0]] = '#'

def create_corridors(level, rooms):

    for i in range (0, 9):
        if rooms[i].door_north != (0, 0):
            put_corridor(level, rooms[i].door_north, rooms[i - 3].door_south)
        if rooms[i].door_south != (0, 0):
            put_corridor(level, rooms[i].door_south, rooms[i + 3].door_north)
        if rooms[i].door_west != (0, 0):
            put_corridor(level, rooms[i].door_west, rooms[i - 1].door_east)
        if rooms[i].door_east != (0, 0):
            put_corridor(level, rooms[i].door_east, rooms[i + 1].door_west)

def create_level():

    level = []
    rooms = create_rooms()

    for i in range(0, 22):
        level.append(80 * [' '])

    for i in range(0, 9):
        for j in range(0, 22):
            for k in range (0, 80):
                get_char(i, j, k, rooms, level)

    create_corridors(level, rooms)

    return [''.join(i) for i in level]

level = create_level()
for line in level:
    print line

"""
def create_level():
    level = []
    level.append("     ----------------         ------------                --------              ")
    level.append("     |..............+#########+..........|            ####+......|              ")
    level.append("     |..............|         |..........+#############   |......|              ")
    level.append("     ------------+---         -------+----                --------              ")
    level.append("                 #                   #                                          ")
    level.append("                 #                   #############                              ")
    level.append("      ############                               #                              ")
    level.append("      #                                          #         --------------       ")
    level.append("      #                      ########################      |............|       ")
    level.append("  ----+------                #                   #  #      |............|       ")
    level.append("  |.........|                #        ############  #######+............|       ")
    level.append("  |.........|                #        #                    |............|       ")
    level.append("  |.........+#################        #                    |............|       ")
    level.append("  -----------                         #                    ---+----------       ")
    level.append("                                      #                       #                 ")
    level.append("                                      #                       #######           ")
    level.append("                                      #                             #           ")
    level.append("                              --------+--                           #           ")
    level.append("    -----                     |.........+##########        ---------+-----      ")
    level.append("    |...|                   ##+.........|         #########+.............|      ")
    level.append("    |...+#################### -----------                  |.............|      ")
    level.append("    -----                                                  ---------------      ")
    return level

