from hero import Enemy
from random import randint
from create_level_strings import create_level_strings
from create_rooms import create_rooms

def get_random_monster(game, room, monster_list_size, monster_count):
    
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
        monster_index = randint(0, monster_list_size - 1)
        monsters.append(Enemy(monster_x, monster_y, monster_level, monster_index))
    
    return monsters

def spawn_monsters(game, monster_list_size):

    for room in game.level_rooms:
        d100 = randint(0, 100)
        monster_count = (2 if d100 > 90 else 1) if d100 > 40 else 0
        if monster_count:
            for monster in get_random_monsters(game, room, monster_list_size, monster_count):
                game.monsters.append(monster)
        
def create_level(game, monster_list_size):

    game.level_num += 1
    game.rooms = create_rooms()
    game.level = create_level_strings(game.rooms)
    game.monsters = spawn_monsters(game, monster_list_size)
#     reset hidden
#     reset monsters
#     reset items
#     set hero 
#     set stairs
