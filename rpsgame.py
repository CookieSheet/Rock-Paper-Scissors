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

    print("Welcome to Rock, Paper, Scissors")
    user_name = input("Whats your name? ")

    # active = True
    while True:
        score = {user_name: 0, "Computer": 0}  
        menu_input = input("""
                        What would you like to do?
                        - Play game(P)
                        - Change Name(N)
                        - Rules(R)
                        - Quit (Q)
                    """)
        if menu_input.lower() == "r":
            print(""" The Rules of Rock, Paper, Scissors:
                    """)

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
                    # You chose Rock
                    if rps.lower() == 'rock':
                        if comp_shot == 0:
                            print("You Tied")
                        elif comp_shot == 1:
                            score["Computer"] += 1
                            print("You lost")
                        elif comp_shot == 2:
                            print("You Won!")
                            score[user_name] += 1
                     
                    # You chose Paper
                    elif rps.lower() == 'paper':
                        if comp_shot == 0:
                            print("You Win!")
                            score[user_name] += 1
                        elif comp_shot == 1:
                            print("You Tied")
                        elif comp_shot == 2:
                            print("You Lost")
                            score["Computer"] += 1
                     
                    # You chose Scissors
                    elif rps.lower() == 'scissors':
                        if comp_shot == 0:
                            print("You Lost")
                            score["Computer"] += 1
                        elif comp_shot == 1:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 2:
                            print("You Tied")
                     
                    else:
                        print("This is not an option, do you need to see the rules?")

                    print(f"""The Scores are:
                    {user_name}: {score[user_name]}
                    Computer: {score["Computer"]}  """)
                    play_on = input("Whould you like to play again?")

            else:
                print("This is not an option.")

                    
        elif menu_input.lower() == "q":
            break

        else:
            print("This is not an option")


    
rps_game()



