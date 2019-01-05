from random import randint

"""
class Room:
        def __init__(self)
            self.width = randint(4)
            """

def generate_rooms():
    pass

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
