import curses

def draw_level(stdscr, level):
    i = 1
    for line in level:
        stdscr.addstr(i, 0, line)
        i += 1

def draw_items(stdscr, items):
    for item in items:
        stdscr.addstr(item.y, item.x, item.sym)

#def draw_monsters():

def draw(stdscr, game):
    height = 24
    width = 80
    stdscr.clear()

    statusbarstr = "Level:{}  Gold: {}  Hp: {}({})  Str: 16(16)  Arm: 4   Exp: 1/0".format(game.level_num, game.gold, game.hero.hp, game.hero.max_hp)

    stdscr.addstr(0, 0, game.title)
    draw_level(stdscr, game.level)
    stdscr.addstr(height-1, 0, statusbarstr)
    
    draw_items(stdscr, game.items)

    stdscr.addstr(game.hero.y, game.hero.x, "@")
    stdscr.move(game.hero.y, game.hero.x)


    stdscr.refresh()
