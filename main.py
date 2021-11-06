from random import randint
from gameComponents import winLose, gameVars, compare


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Get your weapon: rock✊, paper✋ or scissors✌️: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("Player chose: " + gameVars.player)
    print("Computer chose: " + gameVars.computer)

    compare.choiceCompare()

    print("Player life count: " + str(gameVars.playerLives))
    print("Computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost ｡･ﾟ･(ﾉД`)･ﾟ･｡ \033[0;0m")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won ✧*｡٩(ˊᗜˋ*)و✧*｡ \033[0;0m")

    gameVars.player = False
