import curses
import game_over_screen

def draw_msg(stdscr, game, height, width):

    stdscr.addstr(0, 0, game.title)

def draw_status(stdscr, game, height, width):
    statusbarstr = "Level:{}  Gold: {}  Hp: {}({})  Str: {}({})  Arm: {}   Exp[{}]: {}/{}".format(game.level_num, game.gold, game.hero.hp, game.hero.max_hp, game.hero.str + game.hero.weapon, game.hero.max_str + game.hero.weapon, game.hero.armor,game.hero.lvl, game.hero.xp, game.hero.next_lvl)
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

def draw_end(stdscr, game):
    stdscr.clear()
    stdscr.addstr(0, 0, "you quit at level {} with {} gold pieces :(".format(game.level_num, game.gold))

    stdscr.addstr(23, 0, "PRESS SPACE TO END")
    while ord(' ') != stdscr.getch():
        pass

def draw(stdscr, game):

    height = 24
    width = 80
    stdscr.clear()
    if game.game_over == False :
        draw_msg(stdscr, game, height, width)
        draw_status(stdscr, game, height, width)
        draw_level(stdscr, game)
        draw_items(stdscr, game.items)
        draw_monsters(stdscr, game)
        add_fog(stdscr, game)
        draw_hero(stdscr, game)
    else :
       game.level = game_over_screen.game_over_screen(game)
       draw_level(stdscr, game)

    stdscr.refresh()


def draw_list(stdscr, list_to_print):
    stdscr.clear()
    
    for i, item in enumerate(list_to_print[:22]):
        stdscr.addstr(i, 1, item)

    for i, item in enumerate(list_to_print[22:44]):
        stdscr.addstr(i, 40, item)

