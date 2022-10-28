# The Python Roulette Game

## The roulette game
The main purpose with the code/game was to make an easy to play game with interactions such as placing bets and the choice of color. The game is based of the original roulette found inside casinos and maintains the original structure with red as odd, black as even and green as 0.

[link to website](https://python-roulette.herokuapp.com/)

## This is how the deployd version looks like

place for image when deployd.


## How to play the game

The game offers the player few but crucial choises.
- Pick the color that you want to play
 - The different colors offer different odds
- place your bet
- start the roulette machine
- if you have money left in the bank, play again or stop by typing y/n

## The starting interface

![picture of the start interface of the game](images/startGame.png)

when starting the game this is what you will se
- chose your color between red, black and green
- The input will give an error message if the input is something else

![chosing color](images/choseColor.png)

## Place your stake

![picture displaying the screen when the user can place bet](images/placeBet.png)

This is what the user will se when proceding after the color chose
- place a bet that is smaller then what you have in your bank
- if the user try to type in more than what the user have in the bank they will get an error
- the red and black gives you doubble your money and green gives you 35 times the money

## The final display

![the final page](images/placeBet.png)

the final page
- In the final page the user can chose to continue or end the game
- if the user is out of money the game ends automaticly
- the end page will display the amount of money that is won or the money thats been loss

## Potential future events
- Add more bets that can be played
- add more interactive elements
- add an interface with an roulette board

## Validating the code

The validation of the code has been made through web based python validators and manually
- web based pep8 validator 
- manually in terminal, writing wrong inputs to see what happpens etc
- githubs automatical error and code check

## bugs
- the game crash if user type float or string into stake
- the calculating of profit and adding to bank not appearing in terminal

## fixed bugs
- fixed so that the stake input gives a error message if input = float or string 
- changed the if statement to "in" instead of == 

## This python program was deployd through Code Institutes mock terminal using Heroku
### Step by step deployment
- created a new app in heroku
- made the deployment through heroku plus github
- the deployment is manuall



