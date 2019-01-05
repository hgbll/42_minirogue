import curses

def draw_msg(stdscr, game, height, width):

    stdscr.addstr(0, 0, game.title)

def draw_status(stdscr, game, height, width):
    statusbarstr = "Level:{}  Gold: {}  Hp: {}({})  Str: {}({})  Arm: {}   Exp: {}/10".format(game.level_num, game.gold, game.hero.hp, game.hero.max_hp, game.hero.str, game.hero.max_str, game.hero.armor, game.hero.xp)
    stdscr.addstr(height - 1, 0, statusbarstr)

def draw_hero(stdscr, game):

    stdscr.addstr(game.hero.y + 1, game.hero.x, "@")
    stdscr.move(game.hero.y + 1, game.hero.x)

def draw_level(stdscr, game):

    i = 1
    for line in game.level:
        stdscr.addstr(i, 0, line)
        i += 1

def draw_items(stdscr, items):

    for item in items:
        stdscr.addstr(item.y + 1, item.x, item.sym)

def draw_monsters(stdscr, game):

    for monster in game.monsters:
        stdscr.addstr(monster.y + 1, monster.x, monster.symbol)

def add_fog(stdscr, game):
    for y, line in enumerate(game.hidden):
        for x, t in enumerate(line):
            if t: stdscr.addstr(y + 1, x, " ")

def draw(stdscr, game):

    height = 24
    width = 80
    stdscr.clear()

    draw_msg(stdscr, game, height, width)
    draw_status(stdscr, game, height, width)
    draw_level(stdscr, game)
    draw_monsters(stdscr, game)
    draw_items(stdscr, game.items)
    add_fog(stdscr, game)
    draw_hero(stdscr, game)


    stdscr.refresh()


def draw_list(stdscr, list_to_print):
    stdscr.clear()
    
    for i, item in enumerate(list_to_print):
        stdscr.addstr(i, 1, item) 


    stdscr.addstr(24, 0, "PRESS SPACE TO CONTINUE")
    while ord(' ') != stdscr.getch():
        pass