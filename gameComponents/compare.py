from gameComponents import gameVars

def choiceCompare():

    if gameVars.computer == gameVars.player:
        # tie -nothing else to compare, so it'll exit
        print("\033[2;30;47m Tie! try again (◔ д◔) \033[0;0m")

    elif gameVars.player == "rock":
        if (gameVars.computer == "paper"):
            print("\033[2;30;41m You lose! ┐(´д`)┌ \033[0;0m")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\033[2;30;42m You win! ٩(●ᴗ●)۶ \033[0;0m")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if (gameVars.computer == "scissors"):
            print("\033[2;30;41m You lose! ｡┐(´д`)┌ \033[0;0m")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\033[2;30;42m You win! ٩(●ᴗ●)۶ \033[0;0m")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if (gameVars.computer == "rock"):
            print("\033[2;30;41m You lose! ┐(´д`)┌ \033[0;0m")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\033[2;30;42m You win! ٩(●ᴗ●)۶ \033[0;0m")
            gameVars.computerLives = gameVars.computerLives - 1