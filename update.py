def update(game, key):
    if key in (curses.KEY_UP, curses.KEY_K):
        game.hero.y -= 1
    if key in (curses.KEY_DOWN, curses.KEY_K):
        game.hero.y += 1
    if key in (curses.KEY_LEFT, curses.KEY_H):
        game.hero.x -= 1
    if key in (curses.KEY_RIGHT, curses.KEY_L):
        game.hero.x += 1
