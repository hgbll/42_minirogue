import hero
from random import randint
from create_level_strings import create_level_strings
from create_rooms import create_rooms

def get_random_monsters(game, room, monster_count):
    
    monsters = []

    for i in range (0, monster_count):

        not_unique_pos = 1
        while not_unique_pos:
            not_unique_pos = 0
            monster_x = randint(room.box['min_x'], room.box['max_x'])
            monster_y = randint(room.box['min_y'], room.box['max_y'])
            for monster in monsters:
                if monster.x == monster_x and monster.y == monster_y:
                    not_unique_pos = 1
        monster_level = randint(1, game.level_num)
        monster_index = randint(0, 4) # This line needs to be modified if enemy list size changes
        monsters.append(hero.Enemy(monster_x, monster_y, monster_level, monster_index))
    
    return monsters

def spawn_monsters(game):

    for room in game.rooms:
        d100 = randint(0, 100)
        monster_count = (2 if d100 > 90 else 1) if d100 > 40 else 0
        if monster_count:
            for monster in get_random_monsters(game, room, monster_count):
                game.monsters.append(monster)
        
def place_hero(game):

    not_unique_pos = 1
    i = randint(0, 8)
    while not_unique_pos:
        not_unique_pos = 0
        game.hero.x = randint(game.rooms[i].box['min_x'], game.rooms[i].box['max_x'])
        game.hero.y = randint(game.rooms[i].box['min_y'], game.rooms[i].box['max_y'])
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y:
                not_unique_pos = 1

def create_level(game):

    game.level_num += 1

    game.monsters = []
    game.items = []
    game.hidden = [[False] * 80 for i in range(22)]

    game.rooms = create_rooms()
    game.level = create_level_strings(game.rooms)

    spawn_monsters(game)
    place_hero(game)
