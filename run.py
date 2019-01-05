import sys,os
import curses
import create_level
import draw
import hero
import update
import objects

class Game:
    def __init__(self):
        #self.monsters = [Monster(2,3,'B')]
        self.items = [objects.Treasure(11, 2), objects.Food(33, 20)]
        self.hero = hero.Hero(15,21,1)
        self.level_num = 1
        self.gold = 0
        self.title = ""
        self.level = create_level.create_level()

def other_keys(stdscr, key, game):
    if key == ord('?'):
        game.title = "Which character?"
        draw.draw(stdscr, game)
        k = stdscr.getch()
    elif key == ord('i'):
        game.title = "Show inventory"
    elif key == ord('e'):
        food = [x for x in game.hero.inventory if isinstance(x, objects.Food)]
        if len(food) > 0:
            game.hero.hunger = 500
            game.hero.inventory.remove(food[0])
            game.title = "you ate some awful scraps and feel better now"
        else:
            game.title = "you have no food left"
    else:
        return 0
    return 1

def run(stdscr):
    key = 0

    game = Game()

    stdscr.clear()
    stdscr.refresh()

    while True:
        if not other_keys(stdscr, key, game):
            update.update(game, key)
        draw.draw(stdscr, game)

        key = stdscr.getch()
        game.title = ""

def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
