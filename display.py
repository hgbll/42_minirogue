import sys,os
import curses

class Game:
    def __init__(self):
        #self.monsters = [Monster(2,3,'B')]
        #self.hero = Hero()
        self.level = 1
        self.gold = 0
        self.title = ""
        #self.map = get_level()


def options(stdscr, key, game):
    if key == ord('?'):
        game.title = "Which character?"
        display(stdscr, game)
        k = stdscr.getch()



def display(stdscr, game):
    height = 24
    width = 80
    stdscr.clear()

    title = game.title
    statusbarstr = "test"#"Level:{}  Gold:{}     Hp: {}({})  Str: 16(16)  Arm: 4   Exp: 1/0".format(game.level, game.gold, game.hero.hp)

    #draw_level(stdscr, level)

    stdscr.addstr(0, 0, title)
    stdscr.addstr(height-1, 0, statusbarstr)



    # Refresh the screen
    stdscr.refresh()


def run(stdscr):
    key = 0

    game = Game()

    stdscr.clear()
    stdscr.refresh()

    while True:
        #if not options(key)
        options(stdscr, key, game)
        #update(game, key)
        display(stdscr, game)

        key = stdscr.getch()
        game.title = ""




def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()