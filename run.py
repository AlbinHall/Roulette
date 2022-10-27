import random
import time

red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
green = [0]
player_choice = ""
bank = 500
numbers_combined = 36
def Choice_of_color():
    """
    function that makes an input for the user to chose their color they want to bet on.
    """
    global player_choice
    global red
    global black
    global green

    input_color = input("Choose your color: ").lower()

    if input_color == "red":
        player_choice = red
        print("Red is your choice\n")
    elif input_color == "black":
        player_choice = black
        print("Black is your choice\n")
    elif input_color == "green":
        player_choice = green
        print("Green is your choice\n")
    else:
        print("pick beetween red, black and green")
        Choice_of_color()
    
    print(f'Your numbers is: {player_choice}\n')
    return player_choice


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

    print(f'The winning number is {numbers_combined}')


#def the_bank():


#def calculate_the_stake():


#def losing_the_bet


#def main()

player_start_game = Choice_of_color()
random_number_selector()
