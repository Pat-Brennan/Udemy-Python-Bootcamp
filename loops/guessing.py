
# * Guessing Game!

# ? Write a simple guessing game where the computer generates a random number
# ? And you try to guess what it is!

import random

number = random.randint(1, 3)
guess = None


while number != guess:
    print("Guess that number between 1, and 3!!")
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Higher! Higher!')
    elif guess > number:
        print('Lower! Lower!')
    else:
        print('Yooou guessed it!')
print(number)