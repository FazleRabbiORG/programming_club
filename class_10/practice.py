#Practice class for Functions of python
#rock paper scissors game without using functions

import random
ls = ["rock", "paper", "scissors"]

def game():
    print("Welcome to the game of Rock, Paper, Scissors")
    print("You will be playing against the computer")
    print("The first to win 3 times will be the winner")
    print("Good Luck!")
    print("")

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player = input("Enter your choice: ").lower()
        computer = random.choice(ls)
        print("Computer chose: ", computer)

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player == "paper":
            if computer == "scissors":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        elif player == "scissors":
            if computer == "rock":
                print("You lose!")
                computer_score += 1
            else:
                print("You win!")
                player_score += 1
        else:
            print("That's not a valid play. Check your spelling!")

        print("Player Score: ", player_score)
        print("Computer Score: ", computer_score)
        print("")

    if player_score == 3:
        print("Congratulations! You are the winner!")
    else:
        print("Sorry, you lost. Better luck next time!")

    print("")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")

game()
