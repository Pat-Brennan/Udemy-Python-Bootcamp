import random

# * Rock, Paper, Scissors!

print('... Rock ...')
print('... Paper ...')
print('... Scissors ...')

print('Player:')
player = input().lower()

print('Computer:')
comp = random.randint(0, 2)
if comp == 0:
    comp = "rock"
elif comp == 1:
    comp = "paper"
elif comp == 2:
    comp = "scissors"
print(comp)

if player == comp:
    print("DRAWWW!")
elif player == "rock":
    if comp == "paper":
        print("Computer Wins!")
    elif comp == "scissors":
        print("Player Wins!")
elif player == "paper":
    if comp == "scissors":
        print("Computer Wins!")
    elif comp == "rock":
        print("Player Wins!")
elif player == "scissors":
    if comp == "rock":
        print("Computer Wins!")
    elif comp == "paper":
        print("Player Wins!")
else:
    print("Something seems to be amiss...")
