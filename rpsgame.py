# Notes
# What does importing clearOutput do?
#
# Initial Greeting
# Whats your name?
# Initial Menu - Play game, change name, Rules
# Play game?  are you ready to play? 
# r/p/s? -
# display point system, winner, loser? 
# Play game? 
#
# How to center text or align in some way for menu display?
# This is Cookie and Hootie's Rock/Paper/Scissors generator
import random 

def rps_game():
    score = {}
    # active = True
    while True:
        print("Welcome to Rock, Paper, Scissors")
        user_name = input("Whats your name? ")        
        menu_input = input("""
                        What would you like to do?
                        - Play game(P)
                        - Change Name(N)
                        - Rules(R)
                        - Quit (Q)
                    """)
        if menu_input.lower() == "r":
            print(""" Our rules statement """)

        elif menu_input.lower() == "n":
            user_name = input("Whats your name? ")

        elif menu_input.lower() == "p":
            play_on = input("Are you ready to play(y/n? ")
            if play_on.lower() == "n":
                print(menu_input)
            elif play_on.lower() == "y":
                game_list = ["Rock!", "Paper", "Scissors"]
                while play_on.lower() == "y":
                    rps = input("One two three shoot! ") # Need to make a list of Rock Paper Scissors
                    comp_shot = random.randint(0,2)
                    print(game_list[comp_shot])

        
        elif menu_input.lower() == "q":
            break

        else:
            print("This is not an option")


    
rps_game()



