import random
import time

red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
green = [0]
player_choice = ""
bank = 500
numbers_combined = 36
stake = 0


def start_game_func():
    """
    funtion that welcomes the player into the game
    """

    print("Welcome to the python roulette game!\n")
    print("You play the game by chosing a color you want to play\n")
    print(f'Red: {red}\nBlack: {black}\nGreen: {green}\n')
    print("After you have picked a color to play on you can place your bet\n")
    print("The odds for all the colors are:\nRed = 2x the money\nBlack = 2x the money\nGreen = 35x the money\n")


def choice_of_color():
    """
    function that makes an input for the user to chose their color they want to bet on.
    """
    global player_choice
    global red
    global black
    global green

    input_color = input("Choose your color:\n").lower()

    if input_color == "red":
        player_choice = red
        print("Red is your choice\n")
        print(f'Your numbers is: {player_choice}\n')
    elif input_color == "black":
        player_choice = black
        print("Black is your choice\n")
        print(f'Your numbers is: {player_choice}\n')
    elif input_color == "green":
        player_choice = green
        print("Green is your choice\n")
        print(f'Your numbers is: {player_choice}\n')
    else:
        print("pick beetween red, black and green\n")
        choice_of_color()
    
    return player_choice


def taking_stake():
    """
    takes the bet that the player wants to play
    """
    global bank
    global stake

    print(f'Your current balance is {bank}')

    while True:
        try:
            stake = int(input("How much do you want to bet?:\n"))
            if stake <= bank:
                print(f'you played {stake} credits on {player_choice}\n')
            else:
                print("You can't bet more money then you own...\n")
                taking_stake()
            break
        except ValueError:
            print("You need to type an whole number\n")
    return stake


def random_number_selector():
    """
    function that returns and makes the choice of random number
    """
    global numbers_combined
    numbers_combined = random.randrange(0, 36)
    print("The roulette is now starting\n")
    time.sleep(2)
    print("The ball is losing speed...\n")
    time.sleep(2)
    if numbers_combined in player_choice:
        print("You won!\n")
    else:
        print("sorry you lost...\n")
    
    print(f'The winning number is {numbers_combined}\n')

    return numbers_combined


def the_bank():
    """
    function that calculate the stakes and what the player wins/loses. returns the current bank balance
    """
    global bank
    global stake
    global numbers_combined

    if numbers_combined in player_choice:
        if player_choice == red:
            stake = stake * 2 - stake
            bank = stake + bank
            print(f'You won {stake} credits! current bank balance is now {bank}\n')
        elif player_choice == black:
            stake = stake * 2 - stake
            bank = stake + bank 
            print(f'You won {stake} credits! current bank balance is now {bank}\n')
        elif player_choice == green:
            stake = stake * 35 - stake
            bank = stake + bank
            print(f'You won {stake} credits! current bank balance is now {bank}\n')
    else:
        bank = bank - stake
        print(f'You lost {stake} and your current bank balance is {bank}\n')
    
    return bank


def bank_empty():
    """
    function that notice if the bank is = 0 and if True closes the game so the user will have to start over
    """
    global bank

    if bank == 0:
        print("Sorry you are out of credit...")
        time.sleep(2)
        exit()


def exit_function():
    """
    Function that gives the user an option to close the game after each time playing
    """
    exit_input = input("Type: 'y' if you want to continue, else type: 'n':\n")

    if exit_input.lower() == "n":
        exit()
    else:
        main()


def main():
    """
    containing all the functions except the start game function
    """
    choice_of_color()
    taking_stake()
    random_number_selector()
    the_bank()
    bank_empty()
    exit_function()


start_game_func()
main()
