import curses

def draw_level(stdscr, level):
    i = 1
    for line in level:
        stdscr.addstr(i, 0, line)
        i += 1

def draw(stdscr, game):
    height = 24
    width = 80
    stdscr.clear()

    title = game.title
    statusbarstr = "test"#"Level:{}  Gold:{}     Hp: {}({})  Str: 16(16)  Arm: 4   Exp: 1/0".format(game.level, game.gold, game.hero.hp)

    draw_level(stdscr, game.level)

    stdscr.addstr(0, 0, title)
    stdscr.addstr(height-1, 0, statusbarstr)

    # Refresh the screen
    stdscr.refresh()
