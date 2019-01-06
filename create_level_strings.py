from random import randint

def draw_line(level, door1, door2, direction):

    if door1[0] == door2[0]:
        steps = range(door1[1] + 1, door2[1])
        for i in steps:
            level[i][door1[0]] = '#'

    if door1[1] == door2[1]:
        steps = range(door1[0] + 1, door2[0])
        for i in steps:
            level[door1[1]][i] = '#'

    else:
        if direction == "right":
            distance_x = abs(door2[0] - door1[0])
            turn = randint(1, distance_x - 1)
            y = door1[1]
            y_step = 1 if door2[1] - door1[1] > 0 else -1
            for x in range(1, distance_x):
                if x == turn:
                    level[y][door1[0] + x] = '#'
                    while y < door2[1] if door2[1] > door1[1] else y > door2[1]:
                        y += y_step
                        level[y][door1[0] + x] = '#'
                else:
                    level[y][door1[0] + x] = '#'

        if direction == "down":
            distance_y = abs(door2[1] - door1[1])
            turn = randint(1, distance_y - 1)
            x = door1[0]
            x_step = 1 if door2[0] - door1[0] > 0 else -1
            for y in range(1, distance_y):
                if y == turn:
                    level[door1[1] + y][x] = '#'
                    while x < door2[0] if door2[0] > door1[0] else x > door2[0]:
                        x += x_step
                        level[door1[1] + y][x] = '#'
                else:
                    level[door1[1] + y][x] = '#'

def get_char(i, j, k, rooms, level):
    
    if (j == rooms[i].anchor_y or j == rooms[i].anchor_y + rooms[i].height) and (k >= rooms[i].anchor_x and k <= rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '-'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k == rooms[i].anchor_x or k == rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '|'

    if (j > rooms[i].anchor_y and j < rooms[i].anchor_y + rooms[i].height) and (k > rooms[i].anchor_x and k < rooms[i].anchor_x + rooms[i].width):
            level[j][k] = '.'

    if (k != 0 and j != 0):
        if (j == rooms[i].door_north[1] and k == rooms[i].door_north[0]):
            level[j][k] = '+' if not rooms[i].no_room else '#'
        if (j == rooms[i].door_west[1] and k == rooms[i].door_west[0]):
            level[j][k] = '+' if not rooms[i].no_room else '#'
        if (j == rooms[i].door_south[1] and k == rooms[i].door_south[0]):
            level[j][k] = '+' if not rooms[i].no_room else '#'
        if (j == rooms[i].door_east[1] and k == rooms[i].door_east[0]):
            level[j][k] = '+' if not rooms[i].no_room else '#'

def put_corridors(level, rooms):

    for i in range (0, 9):
        if rooms[i].door_south != (0, 0):
            draw_line(level, rooms[i].door_south, rooms[i + 3].door_north, "down")
        if rooms[i].door_east != (0, 0):
            draw_line(level, rooms[i].door_east, rooms[i + 1].door_west, "right")

def put_stairs(level, rooms):

    i = randint(0, 8)
    count = 0
    while rooms[i].no_room and count < 10:
        i = randint(0, 8)
        count += 1

    stairs_x = randint(rooms[i].box['min_x'], rooms[i].box['max_x'])
    stairs_y = randint(rooms[i].box['min_y'], rooms[i].box['max_y'])
    rooms[i].has_stairs = 1
    level[stairs_y][stairs_x] = '%'

def create_level_strings(rooms):

    level = []

    for i in range(0, 22):
        level.append(80 * [' '])

    for i in range(0, 9):
        for j in range(0, 22):
            for k in range (0, 80):
                get_char(i, j, k, rooms, level)

    put_corridors(level, rooms)
    put_stairs(level, rooms)

    return [''.join(i) for i in level]
