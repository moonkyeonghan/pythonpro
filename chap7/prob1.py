import random

def background(board):
  for i in range(0, 9, 3):
    print(" | ".join(board[i:i+3]))
    if i < 6:
      print("-" * 9)

def checkwin(board, playermark):
  for i in range(0, 9 ,3):
    if all(board[mark] == playermark for mark in range(i,i+3)):
      return True
  for i in range(3):
    if all(board[mark] == playermark for mark in range(i,9,3)):
      return True
  if all(board[i] == playermark for i in range(0,9,4)) or all(board[i] == playermark for i in range(2,7,2)):
    return True
  return False

def fullboard(board):
  return all(mark != " " for mark in board)

def player_move(board):
  while True:
    move = int(input("Enter your move (0-8): "))
    if 0 <= move <= 8 and board[move] == ' ':
        return move
    else:
      print("Invalid move. Try again.")

def computer_move(board):
  while True:
      move = random.randint(0, 8)
      if board[move] == ' ':
          return move
def main():
  board = [' ' for _ in range(9)]
  players = ['X', 'O']
  firstplayer= input("Do you want to go first? (y/n): ")
  if firstplayer == 'y':
    current_player = "X"
  else:
    current_player = "O"

  print("Welcome to Tic-Tac-Toe!")
  background([str(i) for i in range(9)])
  background(board)

  for _ in range(9):
      if current_player == 'X':
        move = player_move(board)
      else:
        move = computer_move(board)
        
      board[move] = current_player
      background([str(i) for i in range(9)])
      background(board)

      if checkwin(board, current_player):
        if current_player == 'X':
          print("You won!")
          break
        else:
          print("You lost!")
          break
      if fullboard(board):
          print("It's a tie!")
          break

      current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
  main()
