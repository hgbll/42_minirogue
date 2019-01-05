from random import randint

"""
class Room:

    def __init__(self, zone):

        right_border = (zone % 3) * 26 + 26
        bottom_border = (zone / 3) * 7 + 7

        self.anchor_x = right_border - (6 + randint(0, 20))
        self.anchor_y = bottom_border - (5 + randint(0, 2))

        self.width = randint(4, 4 + (right_border - self.anchor_x - 6))
        self.height = randint(4, 4 +  (bottom_border - self.anchor_y - 5))

        self.zone = zone

def get_char(i, j, k, rooms, level):
    
    if (j == rooms[i].anchor_y or j == rooms[i].anchor_y + rooms[i].height) and (k >= rooms[i].anchor_x and k <= rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '-'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k == rooms[i].anchor_x or k == rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '|'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k > rooms[i].anchor_x and k < rooms[i].anchor_x + rooms[i].width):
            level[j][k] = "."

def create_rooms():

    rooms = []
    for i in range(0, 9):
        rooms.append(Room(i))
    return (rooms)

def create_level():

    level = []
    rooms = create_rooms()

    for i in range(0, 22):
        level.append(80 * [' '])

    for i in range(0, 9):
        for j in range(0, 22):
            for k in range (0, 80):
                get_char(i, j, k, rooms, level)

    for room in rooms:
        print "anchor x = " + str(room.anchor_x)
        print "anchor y = " + str(room.anchor_y)
        print "width = " + str(room.width)
        print "height = " + str(room.height)

    return [''.join(i) for i in level]

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
"""


