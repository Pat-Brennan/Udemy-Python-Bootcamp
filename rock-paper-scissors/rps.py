
# * Rock, Paper, Scissors! 

print('... Rock ...')
print('... Paper ...')
print('... Scissors ...')

print('Player 1:')
player1 = input()

print('Player 2:')
player2 = input()

if player1 == "Rock" and player2 == "Scissors":
  print("Player 1 Wins")
elif player1 == "Rock" and player2 == "Paper":
  print("Player 2 Wins")
elif player1 == "Paper" and player2 == "Rock":
  print("Player 1 Wins")
elif player1 == "Paper" and player2 == "Scissors":
  print("Player 2 Wins")
elif player1 == "Scissors" and player2 == "Paper":
  print("Player 1 Wins")
elif player1 == "Scissors" and player2 == "Rock":
  print("Player 2 Wins")
elif player1 == player2:
  print("DRAW!!!")
else:
  print("There seems to be something amiss ...")
