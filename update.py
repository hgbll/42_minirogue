import curses
import objects

def update_monsters_pos(game):
    for monster in game.monsters:
        monster.update(game.hero, game)

def update_player_pos(game, key):

    free_tiles = ['.', '#', '+', '%']
    x = game.hero.x
    y = game.hero.y

    if key == curses.KEY_UP or key == ord('k'):
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y - 1:
                fight(game.hero,monster, game)
                return
        if game.level[game.hero.y - 1][game.hero.x] in free_tiles:
            game.hero.y -= 1

    if key == curses.KEY_DOWN or key == ord('j'):
        for monster in game.monsters:
            if monster.x == game.hero.x and monster.y == game.hero.y + 1:
                fight(game.hero,monster, game)
                return
        if game.level[game.hero.y + 1][game.hero.x] in free_tiles:
            game.hero.y += 1

    if key == curses.KEY_LEFT or key == ord('h'):
        for monster in game.monsters:
            if monster.x == game.hero.x - 1 and monster.y == game.hero.y:
                fight(game.hero,monster, game)
                return
        if game.level[game.hero.y][game.hero.x - 1] in free_tiles:
            game.hero.x -= 1

    if key == curses.KEY_RIGHT or key == ord('l'):
        for monster in game.monsters:
            if monster.x == game.hero.x + 1 and monster.y == game.hero.y:
                fight(game.hero,monster, game)
                return
        if game.level[game.hero.y][game.hero.x + 1] in free_tiles:
            game.hero.x += 1

    
def handle_item(game, item):

    if isinstance(item, objects.Treasure):
        game.gold += item.value
        game.title = "You found {} gold pieces".format(item.value)
    else:
        game.hero.inventory.append(item)
        game.title = "You picked up : " + item.description

def check_items(game):

    new_list = []
    for item in game.items:
        if item.x == game.hero.x and item.y == game.hero.y:
            handle_item(game, item)
        else:
            new_list.append(item)

    game.items = new_list

def lift_fog(game):
    for y in range(-game.hero.view_distance,game.hero.view_distance+1):
        for x in range(-game.hero.view_distance,game.hero.view_distance+1):
            if 0 <= game.hero.y + y < 22 and 0 <= game.hero.x + x < 80:
                game.hidden[game.hero.y + y][game.hero.x + x] = False
    i = game.hero.get_room_index(game)
    if i >= 0:
        room = game.rooms[i]
        for y in range(room.anchor_y, room.anchor_y + room.height + 1):
            for x in range(room.anchor_x, room.anchor_x + room.width + 1):
                game.hidden[y][x] = False

def add_more(game):
    game.stdscr.addstr(0,0," " * 80)
    game.stdscr.addstr(0, 0, game.title)
    game.stdscr.attron(curses.color_pair(1))
    game.stdscr.addstr(0, len(game.title) + 1, "MORE")
    game.stdscr.attroff(curses.color_pair(1))
    game.stdscr.move(game.hero.y + 1, game.hero.x)
    game.stdscr.getch()

def fight(hero,enemy,game):
    enemy.triggered = True
    hero.attack(enemy)
    if game.title != "":
        add_more(game)
    game.title = hero.combat_status
    if enemy.hp <= 0:
        hero.xp += enemy.exp
        game.monsters.remove(enemy)

def update(game, key):
    game.hero.update(game)

    if game.game_over == False and key != 0:
        update_player_pos(game, key)
        update_monsters_pos(game)
    check_items(game)
    lift_fog(game)
