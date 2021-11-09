from random import randint
from gameComponents import winLose, gameVars, compare


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Get your weapon: rock✊, paper✋ or scissors✌️: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    compare.choiceCompare()

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost ｡･ﾟ･(ﾉД`)･ﾟ･｡ ")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won ✧*｡٩(ˊᗜˋ*)و✧*｡ ")

    gameVars.player = False
