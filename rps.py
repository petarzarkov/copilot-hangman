## Made with copilot
## create rock paper scissors game
import random

rps = ["rock", "paper", "scissors"]

def play_rps():
    choice = input("rock, paper, or scissors? ").lower()
    roll = random.choice(rps)

    if choice == roll:
        print("It's a tie!")
    elif choice == "rock" and roll == "scissors":
        print("You win!", choice, "beats", roll)
    elif choice == "paper" and roll == "rock":
        print("You win!", choice, "beats", roll)
    elif choice == "scissors" and roll == "paper":
        print("You win!", choice, "beats", roll)
    else:
        print("You lose!", roll, "beats", choice)

    play_again = input("Play again? (y/n) ").lower()

    if play_again == "y":
        play_rps()
    else:
        print("Thanks for playing!")


play_rps()