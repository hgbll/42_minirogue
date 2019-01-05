import curses

def draw_msg(stdscr, game, height, width):

    stdscr.addstr(0, 0, game.title)

def draw_status(stdscr, game, height, width):

    statusbarstr = "Level:{}  Gold: {}  Hp: {}({})  Str: 16(16)  Arm: 4   Exp: 1/0".format(game.level_num, game.gold, game.hero.hp, game.hero.max_hp)
    stdscr.addstr(height - 1, 0, statusbarstr)

def draw_hero(stdscr, game):

    stdscr.addstr(game.hero.y, game.hero.x, "@")
    stdscr.move(game.hero.y, game.hero.x)

def draw_level(stdscr, game):

    i = 1
    for line in game.level:
        stdscr.addstr(i, 0, line)
        i += 1

def draw_items(stdscr, items):

    for item in items:
        stdscr.addstr(item.y, item.x, item.sym)

def draw_monsters(stdscr, game):

    for monster in game.monsters:
        stdscr.addstr(monster.y, monster.x, monster.symbol)

def draw(stdscr, game):

    height = 24
    width = 80
    stdscr.clear()

    draw_msg(stdscr, game, height, width)
    draw_status(stdscr, game, height, width)
    draw_level(stdscr, game)
    draw_monsters(stdscr, game)
    draw_items(stdscr, game.items)
    draw_hero(stdscr, game)

    stdscr.refresh()
