import curses

def update_monsters_pos(game):
    return (1)

def update_player_pos(game, key):

    free_tiles = ['.', '#', '+']
    x = game.hero.x
    y = game.hero.y

    if key == curses.KEY_UP:
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y - 1:
                #fight
                return
        if game.level[game.hero.y - 2][game.hero.x] in free_tiles:
            game.hero.y -= 1
            update_monsters_pos(game)

    if key == curses.KEY_DOWN:
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y + 1:
                #fight
                return
        if game.level[game.hero.y][game.hero.x] in free_tiles:
            game.hero.y += 1
            update_monsters_pos(game)

    if key == curses.KEY_LEFT:
        for monster in game.monsters:
            if monster.x == game.hero.x - 1 and monster.y == game.hero.y:
                #fight
                return
        if game.level[game.hero.y - 1][game.hero.x - 1] in free_tiles:
            game.hero.x -= 1
            update_monsters_pos(game)

    if key == curses.KEY_RIGHT:
        for monster in game.monsters:
            if monster.x == game.hero.x + 1 and monster.y == game.hero.y:
                #fight
                return
        if game.level[game.hero.y - 1][game.hero.x + 1] in free_tiles:
            game.hero.x += 1
            update_monsters_pos(game)
    
def update(game, key):
    update_player_pos(game, key)

