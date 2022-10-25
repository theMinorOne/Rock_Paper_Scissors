import random
import time

def get_choice(): #method to get random choice of rock paper scissors
    options = ["rock" , "paper", "scissors"] #create rock paper scissors list
    rand_choice = random.choice(options) # select random element from list
    comp = rand_choice

    print("Choose from :",*options)
    user_choice = input("Your selection: ")

    #while loop to ensure the user enters correct input
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Your selection does not match one of the options, please try again")
        print("Choose from :",*options)
        user_choice = input("Your selection: ")
    
    choices = {"player" : user_choice , "computer" : comp} #create choice dictionary with selected choices

    return choices #return choice dictionary


def win_condition(user, comp):
    list = ["Rock...", "Paper..", "Scissors.", "Shoot!!!"]
    print("\nReady?")
    for i in range(4):
        time.sleep(1)
        print(list[i])
    
    time.sleep(1)

    print(f"\nYou chose {user}\nComputer chose {comp}")

    if user == comp:
        return "It's a tie!!"
    
    elif user == "rock":
        if comp == "scissors":
            return "Rock smashes scissors!\n You win!!"
        else:
            return "Paper covers rock!\n You lose..."
    
    elif user == "paper":
        if comp == "rock":
            return "Paper covers rock!\n You win!!"
        else:
            return "Scissors cuts rock!\n You lose..."

    elif user == "scissors":
        if comp == "paper":
            return "Scissors cuts paper!\n You win!!"
        else:
            return "Rock smashes scissors!\n You lose..."

def play_game():
    user_comp_choice = get_choice()
    result = win_condition(user_comp_choice["player"], user_comp_choice["computer"])
    return result
"""
chosen = get_choice()
result = win_condition(chosen["player"], chosen["computer"])
"""

def main():
    print("Welcome ot Rock Paper Scissors!")
    print(play_game())
    replay = input("\nPlay again?\nEnter y to continue: ")
    while replay == "y":
        print(play_game())
        replay = input("\nPlay again?\nEnter y to continue: ")
    print("Thank you for playing!!!")

if __name__ == "__main__":
    main()