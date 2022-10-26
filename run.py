import random
import time

red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
green = [0]
player_choice = ""


def Choice_of_color():
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
    
    return player_choice


#def random_number_selector():


#def the_bank():


#def calculate_the_stake():


#def losing_the_bet


#def main()

Choice_of_color()
print(player_choice)