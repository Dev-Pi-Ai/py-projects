import random
from guesses_data import words

dashes = []
guesses_count = 10

word = random.choice(words)
guesses_left = 10

for i in range(len(word)):
    dashes.append("-")

def get_guess():
    while True:
        guess = str(input("Guess: "))
        if not guess.islower():
            print("All guesses must be lowercase!")
            continue
        if len(guess) > 1:
            print("All guesses must only be one character!")
            continue
        return guess

def update_dashes(guess, word, dashes):
    global guesses_left
    if guess in word:
        print("That letter is in the word")
        for i in range(len(word)):
            if guess in word[i]:
                dashes[i] = guess
    else:
        print("That letter is in the word!")
        guesses_left = guesses_left - 1

while True:
    print(f"{guesses_left} incorrect guesses left.")
    print("".join(dashes))
    update_dashes(get_guess(), word, dashes)
    if guesses_left < 1:
        print(f"You lose! The word was: {word}!")
        break
    if not "-" in dashes:
        print(f"You win! The word was: {word}!")
        break