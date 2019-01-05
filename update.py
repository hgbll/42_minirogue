import curses
import objects

def update_monsters_pos(game):
    for monster in game.monsters:
        monster.move(game.hero, game.level)

def update_player_pos(game, key):

    free_tiles = ['.', '#', '+']
    x = game.hero.x
    y = game.hero.y

    if key == curses.KEY_UP:
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y - 1:
                #fight
                return
        if game.level[game.hero.y - 1][game.hero.x] in free_tiles:
            game.hero.y -= 1
            update_monsters_pos(game)

    if key == curses.KEY_DOWN:
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y + 1:
                #fight
                return
        if game.level[game.hero.y + 1][game.hero.x] in free_tiles:
            game.hero.y += 1
            update_monsters_pos(game)

    if key == curses.KEY_LEFT:
        for monster in game.monsters:
            if monster.x == game.hero.x - 1 and monster.y == game.hero.y:
                #fight
                return
        if game.level[game.hero.y][game.hero.x - 1] in free_tiles:
            game.hero.x -= 1
            update_monsters_pos(game)

    if key == curses.KEY_RIGHT:
        for monster in game.monsters:
            if monster.x == game.hero.x + 1 and monster.y == game.hero.y:
                #fight
                return
        if game.level[game.hero.y][game.hero.x + 1] in free_tiles:
            game.hero.x += 1
            update_monsters_pos(game)
    
def handle_item(game, item):

    if isinstance(item, objects.Treasure):
        game.gold += item.value
        game.title = "you found {} gold pieces".format(item.value)
    else:
        game.hero.inventory.append(item)
        game.title = "you picked up " + item.description

def check_items(game):

    new_list = []
    for item in game.items:
        if item.x == game.hero.x and item.y == game.hero.y:
            handle_item(game, item)
        else:
            new_list.append(item)

    game.items = new_list

def lift_fog(game):
    for y in range(-1,2):
        for x in range(-1,2):
            if 0 <= game.hero.y + y < 22 and 0 <= game.hero.x + x < 80:
                game.hidden[game.hero.y + y][game.hero.x + x] = False

def update(game, key):

    update_player_pos(game, key)
    lift_fog(game)
    check_items(game)
    game.hero.hunger -= 1
    if game.hero.hunger < 100 and not game.hero.weak:
        game.hero.str /= 2
        game.hero.weak = True
