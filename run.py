import sys,os
import curses
import create_level
import draw
import hero
import update
import objects
import commands
import game_over_screen

class Game:
    def __init__(self, stdscr, name):
        self.monsters = []
        self.hero = hero.Hero(0,0,1)
        self.items = [objects.Potion(4,10,1)]
        self.level_num = 0
        self.gold = 0
        self.title = ""
        self.level = []
        self.rooms = []
        self.hidden = [[True] * 80 for i in range(22)]
        self.game_over = False
        self.stdscr = stdscr
        self.name = name
        self.game_over_screen = game_over_screen.game_over_screen(self)

def wait_with_space(stdscr):
    stdscr.addstr(23, 0, "-- press space to continue --")
    while ord(' ') != stdscr.getch():
        pass

def other_keys(stdscr, key, game):
    if key == ord('?'):
        draw.draw_list(stdscr, commands.commands)
        wait_with_space(stdscr)
    elif key == ord('i'):
        if len(game.hero.inventory) == 0:
            game.title = "you have nothing in your inventory"
        else:
            draw.draw_list(stdscr, [item.description for item in game.hero.inventory])
            wait_with_space(stdscr)
    elif key == ord('e'):
        food = [x for x in game.hero.inventory if isinstance(x, objects.Food)]
        if len(food) > 0:
            game.hero.hunger = 300
            game.hero.inventory.remove(food[0])
            game.hero.hp = min(game.hero.hp + 1, game.hero.max_hp)
            game.hero.str = game.hero.max_str
            game.hero.weak = False
            game.title = "you ate some awful scraps and feel better now"
            return 0
        else:
            game.title = "you have no food left"
    elif key == ord('p'):
        potions = [x for x in game.hero.inventory if isinstance(x, objects.Potion)]
        if len(potions) > 0:
            draw.draw_list(stdscr, [ chr(ord('a') + i)+") " + item.description for i, item in enumerate(potions)])
            stdscr.addstr(23, 0, "-- select a potion to drink --")
            k = 0
            while not ord('a') <= k < ord('a') + len(potions):
                k = stdscr.getch()
            game.title = "you drank something delicious and feel regenerated"
            potions[k - ord('a')].take_potion(game)
            game.hero.inventory.remove(potions[k - ord('a')])
            return 0
        else:
            game.title = "you have no potions left"
    elif key == ord('r'):
        scrolls = [x for x in game.hero.inventory if isinstance(x, objects.Scroll)]
        if len(scrolls) > 0:
            draw.draw_list(stdscr, [ chr(ord('a') + i)+") " + item.description for i, item in enumerate(scrolls)])
            stdscr.addstr(23, 0, "-- select a scroll to read --")
            k = 0
            while not ord('a') <= k < ord('a') + len(scrolls):
                k = stdscr.getch()
            scrolls[k - ord('a')].read_scroll(game)
            game.hero.inventory.remove(scrolls[k - ord('a')])
            return 0
        else:
            game.title = "you have no scrolls left"
    elif key == ord('w'):
        items = [i for i in game.hero.inventory if isinstance(i, objects.Weapon)]
        if len(items) == 0:
            game.title = "you have no weapons in your inventory"
        else:
            draw.draw_list(stdscr, [ chr(ord('a') + i)+") " + item.description for i, item in enumerate(items)])
            stdscr.addstr(23, 0, "-- select a weapon to equip --")
            k = 0
            while not ord('a') <= k < ord('a') + len(items):
                k = stdscr.getch()
            game.hero.weapon = items[k - ord('a')].value
            game.hero.inventory.remove(items[k - ord('a')])
            return 0
    elif key == ord('W'):
        items = [i for i in game.hero.inventory if isinstance(i, objects.Armor)]
        if len(items) == 0:
            game.title = "you have no armor in your inventory"
        else:
            draw.draw_list(stdscr, [ chr(ord('a') + i)+") " + item.description for i, item in enumerate(items)])
            stdscr.addstr(23, 0, "-- select an armor to equip --")
            k = 0
            while not ord('a') <= k < ord('a') + len(items):
                k = stdscr.getch()
            game.hero.armor = items[k - ord('a')].value
            game.hero.inventory.remove(items[k - ord('a')])
            return 0
    elif key == ord('>'):
        if game.level[game.hero.y][game.hero.x] == '%':
            create_level.create_level(game)
            return 0
        else:
            game.title = "I see no way down"
    elif key == ord('-'):
        game.hidden =  [[False] * 80 for i in range(22)]
        game.hero.hp = 1000
    elif key in [ord('.'),ord('h'),ord('j'),ord('k'),ord('l'),curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN, 0]:
        return 0
    return 1

def run(stdscr):
    key = 0
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(23, 0, "Rogue's name? ")
    curses.echo()
    name = stdscr.getstr()
    curses.noecho()

    game = Game(stdscr, name)

    create_level.create_level(game)

    stdscr.clear()
    stdscr.refresh()

    while key != ord('Q') and not game.game_over:
        if not other_keys(stdscr, key, game):
            update.update(game, key)
        draw.draw(stdscr, game)

        key = stdscr.getch()
        game.title = ""

    if game.game_over:
        while key != ord('Q') and key != ord('q'):
            key = stdscr.getch()
    else:
        draw.draw_end(stdscr, game)


def main():
    curses.wrapper(run)

if __name__ == "__main__":
    main()
