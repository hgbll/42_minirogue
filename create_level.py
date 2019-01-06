import hero
import objects
from random import randint
from create_level_strings import create_level_strings
from create_rooms import create_rooms


def get_random_monsters(game, room, monster_count):
    
    monsters = []

    for i in range (0, monster_count):
        if len(monsters) + 1 <= room.size:
            not_unique_pos = 1
            while not_unique_pos:
                not_unique_pos = 0
                monster_x = randint(room.box['min_x'], room.box['max_x'])
                monster_y = randint(room.box['min_y'], room.box['max_y'])
                for other_monster in monsters:
                    if other_monster.x == monster_x and other_monster.y == monster_y:
                        not_unique_pos = 1
                    if monster_x == game.hero.x and monster_y == game.hero.y:
                        not_unique_pos = 1
            monster_level = randint(1, game.level_num)
            dice = (randint(0,len(hero.enemy_list)-1) + randint(0,len(hero.enemy_list)-1)) / 2
            coef =  max(0,(game.level_num%3) -1)
            monster_index = min(dice + coef,len(hero.enemy_list)-1)
            monsters.append(hero.Enemy(monster_x, monster_y, monster_level, monster_index))
    
    return monsters

def get_random_items(game, room, item_count, treasure_count):

    items = []

    for i in range(0, item_count + treasure_count):
        if len(items) + 1 <= room.size:

            not_unique_pos = 1
            while not_unique_pos:
                not_unique_pos = 0
                item_x = randint(room.box['min_x'], room.box['max_x'])
                item_y = randint(room.box['min_y'], room.box['max_y'])
                for other_item in items:
                    if other_item.x == item_x and other_item.y == item_y:
                        not_unique_pos = 1
                    if game.level[item_y][item_x] == '%':
                        not_unique_pos = 1

            if treasure_count:
                if randint(0, 1):
                    items.append(objects.Treasure(item_x, item_y))
                else:
                    items.append(objects.Food(item_x,item_y,randint(0, len(objects.food_list) - 1)))
                treasure_count -= 1
            else:
                item_type = objects.item_types[randint(0, len(objects.item_types) - 1)]
                items.append(item_type(item_x, item_y, randint(0, game.level_num)))

    return items

def spawn_monsters(game):

    elite_room = 4 if game.level_num >= 3 else 2

    for room in game.rooms:
        d100 = randint(0, 100)
        monster_count = (elite_room if d100 > 90 else 1) if d100 > 40 else 0
        if monster_count:
            for monster in get_random_monsters(game, room, monster_count):
                game.monsters.append(monster)
        
def spawn_items(game):
    
    treasure_room = 5 if game.level_num >= 2 else 2

    for room in game.rooms:
        d100 = randint(0, 100)
        item_count = (treasure_room if d100 > 95 else 1) if d100 > 60 else 0
        d100 = randint(0, 100)
        treasure_count = (treasure_room if d100 > 95 else 1) if d100 > 50 else 0
        if item_count or treasure_count:
            for item in get_random_items(game, room, item_count, treasure_count):
                game.items.append(item)

def place_hero(game):

    i = randint(0, 8)
    while game.rooms[i].has_stairs:
        i = randint(0, 8)

    not_unique_pos = 1
    while not_unique_pos:
        not_unique_pos = 0
        game.hero.x = randint(game.rooms[i].box['min_x'], game.rooms[i].box['max_x'])
        game.hero.y = randint(game.rooms[i].box['min_y'], game.rooms[i].box['max_y'])
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y:
                not_unique_pos = 1

    game.hero.view_distance = 1

def create_level(game):

    game.level_num += 1

    game.monsters = []
    game.items = []
    game.hidden = [[True] * 80 for i in range(22)]

    game.rooms = create_rooms()
    game.level = create_level_strings(game.rooms)

    spawn_monsters(game)
    spawn_items(game)
    place_hero(game)
