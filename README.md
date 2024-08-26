# Tic-Tac-Toe-Game 🎮

Welcome to the **Tic-Tac-Toe game!🕹️** This is a simple console-based implementation of the classic Tic-Tac-Toe game in Python.<br>

## Table of Contents

- [Overview](#overview-)
- [Features](#features)
- [Installation](#installation-)
- [How to Play](#how-to-play-)
- [Code Overview](#code-overview-)

## Overview 📜

This project is a basic implementation of the Tic-Tac-Toe game where two players take turns marking spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.<br>

 ## Features
◻️ **Player Input:** Enter a number between 1 and 9 to make your move.<br>
◻️ **Computer Move:** The computer selects a random available position.<br>
◻️ **Winning Conditions:** Checks for horizontal, vertical, and diagonal wins.<br>
◻️ **Tie Condition:** Ends the game if the board is full and no winner is found.<br>
◻️ **Board Display:** Shows the current state of the board after each move.<br>

## Installation 🛠️

1. Make sure you have Python 3.x installed on your computer.<br>
2. **Clone the Repository:** Get the code onto your local machine.<br>

       git clone https://github.com/YuiSurbhi/Tic-Tac-Toe-Game.git
       cd Tic-Tac-Toe-Game
      
3. **Run the Script:** Execute the game script with Python.

       python main.py

4. **Play the Game:** Follow the prompts to play. Enter a number between 1 and 9 to make your move!

## How to Play 📝

1. **Start the Game:** Run the Python script to begin the game.<br>

2. **Player Move:**

- You’ll be prompted to enter a number from 1 to 9. Each number corresponds to a position on the board:<br>

      1 | 2 | 3
      ---------
      4 | 5 | 6
      ---------
      7 | 8 | 9

- Choose an empty spot to place your mark. If the spot is already occupied, you'll need to pick another one.<br>

3. **Computer Move:**
- After your move, the computer will make its move automatically.<br>
- The computer selects a random empty spot to place its mark ("O").<br>

4. **Win or Tie:**

- The game checks for a win or tie after each move.<br>
- If a player wins or if all spots are filled (a tie), the game will display the result and end.<br>

## Code Description 📝

◻️ ***'printBoard(board)':*** Displays the current game board.<br>
◻️ ***'playerInput(board)':*** Handles the human player's input.<br>
◻️ ***'computer(board)':*** Chooses a random move for the computer.<br>
◻️ ***'checkHorizontle(board)':*** Checks for horizontal winning conditions.<br>
◻️ ***'checkRow(board)':*** Checks for vertical winning conditions.<br>
◻️ ***'checkDiag(board)':*** Checks for diagonal winning conditions.<br>
◻️ ***'checkTie(board)':*** Checks if the game is a tie (no empty spots left).<br>
◻️ ***'checkWin(board)':*** Determines if there's a winner or if the game should end in a tie.<br>
◻️ ***'switchPlayer(board)':*** Switches turns between the human player ("X") and the computer ("O").<br>
◻️ **Game Loop:** Manages the game flow, including alternating turns and checking the game status. ⏳<br>

