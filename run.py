import sys,os
import curses
import create_level
import draw
import hero

class Game:
    def __init__(self):
        #self.monsters = [Monster(2,3,'B')]
        self.hero = hero.Hero(0,0,1)
        self.level_num = 1
        self.gold = 0
        self.title = ""
        self.level = create_level.create_level()

def options(stdscr, key, game):
    if key == ord('?'):
        game.title = "Which character?"
        draw.draw(stdscr, game)
        k = stdscr.getch()

def run(stdscr):
    key = 0

    game = Game()

    stdscr.clear()
    stdscr.refresh()

    while True:
        #if not options(key)
        options(stdscr, key, game)
        #update(game, key)
        draw.draw(stdscr, game)

        key = stdscr.getch()
        game.title = ""

def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
