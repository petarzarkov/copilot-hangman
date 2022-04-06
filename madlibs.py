## create madlibs game
import random

nouns = ["dog", "cat", "bird", "fish", "lizard", "snake", "turtle", "hamster", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog", "tiger", "bear", "deer", "elephant", "giraffe", "zebra", "panda", "kangaroo", "koala", "pig", "cow", "sheep", "goat", "horse", "penguin", "duck", "chicken", "frog"]

## play game
def play_madlibs():
    player = input("Enter a name: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    noun = random.choice(nouns)
    
    # print story
    print("Once upon a time, there was a " + adjective + " " + noun + " named " + player + ".")
    print("One day, " + player + " decided to " + verb + " " + noun + " in the " + place + ".")
    print("The " + noun + " was so " + adjective + " that " + player + " decided to take it home.")

    # play again
    play_again = input("Play again? (y/n) ").lower()
    
    if play_again == "y":
        play_madlibs()
    else:
        print("Thanks for playing!")


play_madlibs()
