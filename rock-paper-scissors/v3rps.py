import random

# * Rock, Paper, Scissors!

player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f'Player Score: {player_wins} Computer Score: {computer_wins}')
    print('... Rock ...')
    print('... Paper ...')
    print('... Scissors ...')

    print('Player:')
    player = input("Choose your weapon...\n").lower()
    if player == "quit" or player == "q":
        break
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
if player_wins > computer_wins:
    print("YOU ELIMINATED THE AI MENACE!!!")
elif player_wins == computer_wins:
    print("WAR'S CALLED OFF!")
else:
    print("You've failed humanity! May the old faith save us all! ")
print(
    f"FINAL SCORES: Player Score: {player_wins} Computer Score: {computer_wins}")
