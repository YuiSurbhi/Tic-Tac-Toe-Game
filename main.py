import random     # Import random for the computer bot's move

# Initialize the game board with "-" indicating empty spots 
board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

currentPlayer = "X"    # currentPlayer; start with "X"
winner = None        # To keep track of the winner 
gameRunning = True     # Game status flag 

# Printing the current state of the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Display the initial game Board
printBoard(board)

# Take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9 : "))     # Prompt user for input (1-9)
    # Check if the input is valid and the chosen position is available
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": 
        board[inp-1] = currentPlayer     # PLace the player's marks on the board
    else:
        print("🚫 Oops player is already in that spot!")

# Handle Computer move
def computer(board):
    while currentPlayer == "O":     # Perform this if it's the computer's turn
        position = random.randint(0, 8)     # Random choose a position (0, 8)
        if board[position] == "-":     # Check if the position is available
            board[position] = "O"     # Place the computer's on the board
            switchPlayer(board)     # Switch to other player
            break     # Exit the loop after a valid move

# Check horizontal winning conditions
def checkHorizontle(board):
    global winner
    # Check each row for a win condition
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# Check vertical winning conditions    
def checkRow(board):
    global winner
    # Check each column for a win condition
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# Check diagonal winning conditions    
def checkDiag(board):
    global winner
    # Check both diagonals for a win condition
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
# Check for a tie (no empty spot left)
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("🤝It is a tie!")     # Notify that the game is a tie
        gameRunning = False     # End the game

# Check for a winner
def checkWin(board):
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"🏆 The winner is {winner}!")    # Announce the winner

# Switch the player
def switchPlayer(board):
    global currentPlayer
    # Switch the current player between "X" and "O"
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Main game loop
while gameRunning:
    printBoard(board)      # Display board
    playerInput(board)     # Get input from the player
    checkWin(board)     # Check for a win
    checkTie(board)      # Check for a tie
    if not gameRunning:
        break      # Exit the loop if the game has ended
    switchPlayer(board)      # Switch to the next player
    computer(board)     # Let the computer make a move
    checkWin(board)     # Check for a win after the computer's move
    checkTie(board)     # Check for a tie after the computer's move
