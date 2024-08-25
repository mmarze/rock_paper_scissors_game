"""
The Rock-Paper-Scissors game

Rules:
Rock smashes scissors. Rock crushes Lizard.
Paper covers rock. Paper disproves Spock.
Scissors cut paper. Scissors decaptivated Lizard.
Lizard poisons Spock. Lizard eats Paper.
Spock smashes Scissors. Spock waporizes Rock.
"""

import random 
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4
    
    
victories = {
    Action.Rock: [Action.Scissors, Action.Lizard],
    Action.Paper: [Action.Rock, Action.Spock],
    Action.Scissors: [Action.Paper],
    Action.Lizard: [Action.Spock, Action.Paper], 
    Action.Spock: [Action.Scissors, Action.Rock]}


def user_action():
    print('\n\tWelcome to the game!')
    choices = [f"{action.name}[{action.value}]" for action in Action]
    return Action(int(input(f"Enter a choice: {', '.join(choices)}: ")))


def computer_action():
    computer_action = Action(random.randint(0, 2))
    print(f"\tComputer chose {computer_action}.")
    return computer_action


def who_wins(user, computer):
    defeats = victories[user]
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif computer in defeats:
        print(f"{user.name} defeats {computer.name}! You win!")
    else:
        print(f"{computer.name} defeats {user.name}! You lose!")


def single_game():
    try:
        user_choice = user_action()
        computer_choice = computer_action()
        who_wins(user_choice, computer_choice)
    except ValueError:
        print(f"ERROR! Invalid selection. Enter a value in range [0, {len(Action) - 1}]!")
    

def main():
    while True:
        single_game()
        play_again = input('Play again? [y/n] ')
        if not play_again.lower() == 'y':
           break 
       
        
if __name__ == '__main__':
    main()
    
