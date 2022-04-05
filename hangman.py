import random

class Hangman:
    def __init__(self, words: list[str]):
        self.words = words
        self.init()

    def init(self):
        self.word = random.choice(self.words)
        self.letters = list(self.word)
        self.guess = ""
        self.guesses = []
        self.guess_count = 0
        self.number_of_guesses = 6
        self.playing = True

    @property
    def guess_progress(self):
        return "".join([ letter if letter in self.guesses else "_" for letter in self.letters ])

    def start(self):
        print("===================")
        print("Welcome to Hangman!")
        print("The word has", len(self.word), "letters")
        print("You have", self.number_of_guesses, "guesses")
        print("Good luck!")
        print("===================")

        while self.playing:
            self.guess = input("Guess a letter: ")
            self.guess = self.guess.lower()

            if len(self.guess) != 1:
                print("You can only guess a single letter!")
            elif self.guess in self.guesses:
                print("You already guessed the letter", self.guess)
            elif self.guess not in "abcdefghijklmnopqrstuvwxyz":
                print("You can only guess letters!")
            else:
                self.guesses.append(self.guess)
                if self.guess in self.word:
                    print("Good job!", self.guess, "is in the word", self.guess_progress)
                else:
                    print("Sorry", self.guess, "is not in the word", self.guess_progress)
                    self.guess_count += 1
                    print("You have", self.number_of_guesses - self.guess_count, "guesses left")

            self.print_hangman(self.guess_count)

            if self.guess_count == self.number_of_guesses:
                print("Sorry, you ran out of guesses. The word was", self.word)
                self.play_again()

            if self.guess_progress == self.word:
                print("Congratulations, you guessed the word!")
                print("You guessed the word with", self.guess_count, "mistakes")
                print("The word was", self.word)
                self.play_again()

    def play_again(self):
        again = input("Do you want to play again? (y/n) ")
        if again == "y":
            self.init()
            self.start()

        print("Thanks for playing!")
        self.playing = False

    def print_hangman(self, count: int):
        states = [
            '''
            +---+
                |
                |
                |
                ===
            ''', 
            '''
            +---+
            O   |
                |
                |
                ===
            ''',
            '''
            +---+
            O   |
            |   |
                |
                ===
            ''',
            '''
            +---+
            O   |
           /|   |
                |
                ===
            ''',
            '''
            +---+
            O   |
           /|\  |
                |
                ===
            ''',
            '''
            +---+
            O   |
           /|\  |
           /    |
                ===
            ''',
            '''
            +---+
            0   |
           /|\  |
           / \  |
                ===
            '''
        ]
        print(states[count])


hangman = Hangman([
    "absence",
    "abuse",
    "account",
    "accident","beneath","bend","benefit","biology",
    "bitter","candidate","campaign","camera","capacity","capture",
    "deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient",
    "supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle",
    "global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense",
    "nobody","turmeric","utilize","sashimi",
    "reconfigure","wheat"
    "yellowish","zone"
    ])

hangman.start()