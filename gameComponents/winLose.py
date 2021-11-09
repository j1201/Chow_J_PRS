from gameComponents import gameVars


def winorlose(status):
    print("\033[2;30;46m You " + status)

    choice = input("Do you want to play again٩(｡・ω・｡)و? y/n: ")

    if choice == "n":
        print("========== Alright. See ya! ╮(╯_╰)╭ ==========")
        exit()
    elif choice == "y":
        gameVars.playerLives = 2
        gameVars.computerLives = 2
        gameVars.player = False
