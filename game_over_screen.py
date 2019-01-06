def game_over_screen(game):
    name = game.name
    if len(name) > 18:
        name = name[:18]
    game_over = []
    game_over.append("                                                           ")
    game_over.append("                                                           ")
    game_over.append("                                                           ")
    game_over.append("                                                           ")
    game_over.append("                                   __________              ")
    game_over.append("                                  /          \             ")
    game_over.append("                                 /    REST    \            ")
    game_over.append("                                /      IN      \           ")
    game_over.append("                               /     PEACE      \          ")
    game_over.append("                              /                  \         ")
    game_over.append("                              |                  |         ")
    game_over.append("                              |      level       |         ")
    game_over.append("                              |        "+ str(game.hero.lvl)+"         |         ")
    game_over.append("                              |"+      name.center(18, ' ')  +          "|         ")
    game_over.append("                              |                  |         ")
    game_over.append("                             *|     *  *  *      | *       ")
    game_over.append("                     ________)/\\_//(\/(/\)/\//\/|_)_______")
    game_over.append("                                                           ")
    game_over.append("                               Press 'Q' to exit")
    return game_over