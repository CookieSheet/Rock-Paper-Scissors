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

    print("\nWelcome to Rock, Paper, Scissors")
    score = {"Computer": 0}
    user_name = input("\nWhats your name? ")
    score[user_name] = 0

    working = True
    while working:
        menu_input = input(f"""
                        {user_name} what would you like to do?
                        - Play game(P)
                        - Change Name(N)
                        - Rules(R)
                        - Quit (Q)
                    """)
        if menu_input.lower() == "r":
            print(""" 
                      The Rules of Rock, Paper, Scissors, Lava, Rain:
                      
                      Rock Beats Scissors and Lava
                      Scissors beats Paper and Rain
                      Paper beats Rock and Rain
                      Lava beats Scissors and Paper
                      Rain beats Rock and  Lava


                      Choose your weapon wisely!
                    """)

        elif menu_input.lower() == "n":
            user_name = input("Whats your name? ")
            score[user_name] = 0
            score["Computer"] = 0

        elif menu_input.lower() == "p":
            play_on = input("Are you ready to play(y/n?) ")
            if play_on.lower() == "n":
                print(menu_input)
            elif play_on.lower() == "y":
                game_list = ["Rock!", "Paper!", "Scissors!", "Lava!", "Rain!"]
                while play_on.lower() == "y":
                    rps = input("One two three shoot! ") 
                    comp_shot = random.randint(0,4)           #random generator
                    print(game_list[comp_shot])
                                                              
                    if rps.lower() == 'rock':                 # You choose Rock
                        if comp_shot == 0:
                            print("You Tied")
                        elif comp_shot == 1:
                            score["Computer"] += 1
                            print("You lost")
                        elif comp_shot == 2:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 3:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 4:
                            score["Computer"] += 1
                            print("You lost")
                                                  
                    elif rps.lower() == 'paper':               # You chose Paper
                        if comp_shot == 0:
                            print("You Win!")
                            score[user_name] += 1
                        elif comp_shot == 1:
                            print("You Tied")
                        elif comp_shot == 2:
                            print("You Lost")
                            score["Computer"] += 1
                        elif comp_shot == 3:
                            print("You Lost")
                            score["Computer"] += 1
                        elif comp_shot == 4:
                             print("You Win!")
                             score[user_name] += 1
                     
                    elif rps.lower() == 'scissors':            # You chose Scissors
                        if comp_shot == 0:
                            print("You Lost")
                            score["Computer"] += 1
                        elif comp_shot == 1:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 2:
                            print("You Tied")
                        elif comp_shot == 3:
                            print("You Lost")
                            score["Computer"] += 1
                        elif comp_shot == 4:
                             print("You Win!")
                             score[user_name] += 1
                            

                    elif rps.lower() == 'lava':               # You chose Lava
                        if comp_shot == 0:
                            print("You Lose!")
                            score["Computer"] += 1
                        elif comp_shot == 1:
                            print("You Won! ")
                            score[user_name] += 1
                        elif comp_shot == 2:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 3:
                            print("You Tied")
                        elif comp_shot == 4:
                             print("You Lose!")
                             score["Computer"] += 1

                    elif rps.lower() == 'rain':               # You chose Rain
                        if comp_shot == 0:
                            print("You Lose!")
                            score["Computer"] += 1
                        elif comp_shot == 1:
                            print("You Won! ")
                            score[user_name] += 1
                        elif comp_shot == 2:
                            print("You Won!")
                            score[user_name] += 1
                        elif comp_shot == 3:
                            print("You Lose")
                            score["Computer"] += 1
                        elif comp_shot == 4:
                            print("You Tied!")
                        
                     
                    else:
                        print("This is not an option, do you need to see the rules?")

                    print(f"""The Scores are:
                    {user_name}: {score[user_name]}
                    Computer: {score["Computer"]}  """)
                    play_on = input("Whould you like to play again?(y,n) ")

            else:
                print("This is not an option.")

                    
        elif menu_input.lower() == "q":
            working = False

        else:
            print("This is not an option")


    
rps_game()



