import random

# * Rock, Paper, Scissors!

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
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
            computer_wins += 1
        elif comp == "scissors":
            print("Player Wins!")
            player_wins += 1
    elif player == "paper":
        if comp == "scissors":
            print("Computer Wins!")
            computer_wins += 1
        elif comp == "rock":
            print("Player Wins!")
            player_wins += 1
    elif player == "scissors":
        if comp == "rock":
            print("Computer Wins!")
            computer_wins += 1
        elif comp == "paper":
            print("Player Wins!")
            player_wins += 1
    else:
        print("Something seems to be amiss...")
