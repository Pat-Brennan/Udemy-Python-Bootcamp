
# * Rock, Paper, Scissors!

print('... Rock ...')
print('... Paper ...')
print('... Scissors ...')

print('Player 1:')
player1 = input()

print("*** NO CHEATING YOU CHEATER!!! ***'\n \n' " * 20)

print('Player 2:')
player2 = input()

# if player1 == "Rock" and player2 == "Scissors":
#   print("Player 1 Wins")
# elif player1 == "Rock" and player2 == "Paper":
#   print("Player 2 Wins")
# elif player1 == "Paper" and player2 == "Rock":
#   print("Player 1 Wins")
# elif player1 == "Paper" and player2 == "Scissors":
#   print("Player 2 Wins")
# elif player1 == "Scissors" and player2 == "Paper":
#   print("Player 1 Wins")
# elif player1 == "Scissors" and player2 == "Rock":
#   print("Player 2 Wins")
# elif player1 == player2:
#   print("DRAW!!!")
# else:
#   print("There seems to be something amiss ...")


# * Refactored
# ? Basically gets rid of all the 'ands'

if player1 == player2:
    print("DRAWWW!")
elif player1 == "Rock":
    if player2 == "Paper":
        print("Player 2 Wins!")
    elif player2 == "Scissors":
        print("Player 1 Wins!")
elif player1 == "Paper":
    if player2 == "Scissors":
        print("Player 2 Wins!")
    elif player2 == "Rock":
        print("Player 1 Wins!")
elif player1 == "Scissors":
    if player2 == "Rock":
        print("Player 2 Wins!")
    elif player2 == "Paper":
        print("Player 1 Wins!")
else:
  print("Something seems to be amiss...")