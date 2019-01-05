import sys,os
import curses
import create_level
import draw
import hero
import update
import objects

class Game:
    def __init__(self):
        self.monsters = [hero.Enemy(3,15,1,0)]
        self.hero = hero.Hero(65,21,1)
        self.items = [objects.Treasure(11, 2), objects.Food(33, 19), objects.Armor(60, 11, 1)]
        self.level_num = 1
        self.gold = 0
        self.title = ""
        self.level = create_level.create_level()
        self.hidden = [[True] * 80 for i in range(22)]

def other_keys(stdscr, key, game):
    if key == ord('?'):
        game.title = "Which character?"
        draw.draw(stdscr, game)
        k = stdscr.getch()
    elif key == ord('i'):
        if len(game.hero.inventory) == 0:
            game.title = "you have nothing in your inventory"
        else:
            draw.draw_list(stdscr, [item.description for item in game.hero.inventory])
    elif key == ord('e'):
        food = [x for x in game.hero.inventory if isinstance(x, objects.Food)]
        if len(food) > 0:
            game.hero.hunger = 500
            game.hero.inventory.remove(food[0])
            game.hero.hp = min(game.hero.hp + 1, game.hero.max_hp)
            game.hero.str = game.hero.max_str
            game.hero.weak = False
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
