# 🎮 Tic-Tac-Toe-Game 

Welcome to the **Tic-Tac-Toe game!🕹️** This is a simple console-based implementation of the classic Tic-Tac-Toe game in Python.<br>

## Table of Contents

- [Description](#description-)
- [Features](#features-)
- [Installation](#installation-)
- [How to Play](#how-to-play-)
- [Functions](#functions-)
- [Example](#example-)

## Description 📜

This project is a basic implementation of the Tic-Tac-Toe game where two players take turns marking spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. This is a simple command-line implementation of the classic Tic-Tac-Toe game. The game allows one player to compete against the computer. The player plays as "X" while the computer plays as "O".<br>

 ## Features ✨
 
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

## How to Play 🚀

1. **🎮 Game Start:**
   - The game begins with an empty 3x3 grid represented by the following layout:<br>
     ```
     - | - | -
     ----------
     - | - | -
     ----------
     - | - | -
     ```

2. **🕹️ Player's Turn:**
   - The player is prompted to enter a number between 1 and 9, which corresponds to a position on the board:<br>
     ```
     1 | 2 | 3
     ----------
     4 | 5 | 6
     ----------
     7 | 8 | 9
     ```
   - The player's input places an **"X"** on the board in the chosen position.<br>

3. **🤖 Computer's Turn:**
   - After the player’s move, the computer automatically takes its turn by placing an **"O"** in a random available spot on the board.<br>

4. **🏆 Winning the Game:**
   - The game checks for a winner after each turn. The first player to align three marks (horizontally, vertically, or diagonally) wins the game.<br>
   - If all spots are filled and there is no winner, the game results in a tie.<br>

5. **🔚 Game End:**
   - The game announces the winner or a tie and then ends.<br>


## Functions ⚙️

- `printBoard(board)`: 🖥️ Prints the current state of the game board.
- `playerInput(board)`: 🎯 Takes input from the player and places **"X"** on the chosen spot if it’s valid.
- `computer(board)`: 🤖 Randomly selects an available spot for the computer's move and places **"O"**.
- `checkHorizontle(board)`: ➡️ Checks for a horizontal win.
- `checkRow(board)`: ⬆️ Checks for a vertical win.
- `checkDiag(board)`: 🔀 Checks for a diagonal win.
- `checkTie(board)`: ⚖️ Checks if the game is a tie.
- `checkWin(board)`: 🏆 Checks if there is a winner.
- `switchPlayer(board)`: 🔄 Switches the turn between the player and the computer.

## Example 🎉

- Enter a number 1-9 : 1
```
X | - | -
----------
- | - | -
----------
- | - | -
```
- Now the computer will make the move randomly.<br>
```plaintext
X | - | -
----------
- | O | -
----------
- | - | -
```
- Enter a number 1-9 : 5<br>
 🚫 Oops, player is already in that spot!
```
X | - | -
----------
- | O | -
----------
- | - | -
```
