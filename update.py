import curses
import objects

def update_player(game, key):

    valid_tiles = ['.', '#', '+']
    x = game.hero.x
    y = game.hero.y

    if (key == curses.KEY_UP
            and game.level[game.hero.y - 2][game.hero.x] in valid_tiles):
        game.hero.y -= 1
        return (True)

    if (key == curses.KEY_DOWN
            and game.level[game.hero.y][game.hero.x] in valid_tiles):
        game.hero.y += 1
        return (True)

    if (key == curses.KEY_LEFT
            and game.level[game.hero.y - 1][game.hero.x - 1] in valid_tiles):
        game.hero.x -= 1
        return (True)

    if (key == curses.KEY_RIGHT
            and game.level[game.hero.y - 1][game.hero.x + 1] in valid_tiles):
        game.hero.x += 1
        return (True)

    game.hero.x=max(2, game.hero.x)
    game.hero.x=min(77, game.hero.x)
    game.hero.y=max(2, game.hero.y)
    game.hero.y=min(21, game.hero.y)
    
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

def update(game, key):
    update_player(game, key)
    check_items(game)

    game.hero.hunger -= 1

