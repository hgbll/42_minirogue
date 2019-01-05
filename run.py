import sys,os
import curses
import create_level
import draw
import hero
import update

class Game:
    def __init__(self):
        self.monsters = [hero.Enemy(65,20,1,0)]
        self.hero = hero.Hero(65,21,1)
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
        update.update(game, key)
        draw.draw(stdscr, game)

        key = stdscr.getch()
        game.title = ""

def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
