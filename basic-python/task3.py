# Modify the program that mixes the letters, so that each word has a hint. The user should
# be able to see the hint if they get stuck in deadlock. Add the scoring system which
# gives the reward for solving without hint.

import random

words = ("plant", 'mug', "being", "chocolate", "fire")
word = random.choice(words)

guesses = ''
score = 3

turns = 10

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:

            print(char),

        else:

            print("_"),
            failed += 1

    if failed == 0:
        print("You won with score = ", + score)
        break
    print()
    guess = input("Guess a letter:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

    elif guess in word:
        print("Right")

    if turns == 1:
        score = 0
        print("You lose your additional point because you need a hint")
        if word == "plant":
            print("Produces oxygen")

        elif word == "mug":
            print("Used for tea")

        elif word == "being":
            print("eg. alive")

        elif word == "chocolate":
            print("sweet")

        elif word == "fire":
            print("red and warm")

    print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You Loose")
