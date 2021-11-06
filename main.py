from random import randint
from gameComponents import winLose, gameVars


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Get your weapon: rock✊, paper✋ or scissors✌️: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    if gameVars.computer == gameVars.player:
        # tie -nothing else to compare, so it'll exit
        print("Tie! try again (◔ д◔)")

    elif gameVars.player == "rock":
        if (gameVars.computer == "paper"):
            print("You lose! ┐(´д`)┌")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! ٩(●ᴗ●)۶")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if (gameVars.computer == "scissors"):
            print("You lose! ｡┐(´д`)┌ ")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! ٩(●ᴗ●)۶ ")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if (gameVars.computer == "rock"):
            print("You lose! ┐(´д`)┌ ")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! ٩(●ᴗ●)۶ ")
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost ｡･ﾟ･(ﾉД`)･ﾟ･｡ ")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won ✧*｡٩(ˊᗜˋ*)و✧*｡ ")

    gameVars.player = False
