## create magic 8 ball game
import random

magic = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

def play_magic():
    question = input("Ask a question: ")
    answer = random.choice(magic)
    print(answer)
    play_again = input("Play again? (y/n) ").lower()

    if play_again == "y":
        play_magic()
    else:
        print("Thanks for playing!")

play_magic()