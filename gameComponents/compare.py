from gameComponents import gameVars

def choiceCompare():

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