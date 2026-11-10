# Project - ❌ Tic Tac Toe Game ⭕

## 📌 Description

Build a Python-based **Tic Tac Toe Game** with a graphical user interface using the Tkinter library.

The game is played between two players, X and O, on a 3×3 grid. Players take turns marking empty boxes. The program checks for horizontal, vertical, and diagonal winning combinations and declares the winner. If all nine boxes are filled without a winner, the game ends in a tie.

## ✨ Features

- Two-player gameplay (X and O).
- Interactive 3×3 game board.
- Graphical user interface using Tkinter.
- Automatically switches turns between players.
- Detects horizontal, vertical, and diagonal winning combinations.
- Highlights the winning combination.
- Displays a popup message when a player wins or the game ends in a tie.
- Prevents players from marking an already occupied box.
- Prevents further moves after the game is over.
- Restart button to start a new game.
- Automatically centers the game window on the screen.

## 🔄 Program Flow

1. Initialize the game with two players: X and O.
2. Create the main game window using Tkinter.
3. Display a 3×3 grid of buttons.
4. Ask the current player to select an empty box.
5. Display the player's mark (X or O) in the selected box.
6. Switch the turn to the other player.
7. Check for a winner after every move.
8. Check horizontal, vertical, and diagonal combinations.
9. If a player wins, highlight the winning combination and display a message.
10. If all nine boxes are filled without a winner, declare a tie.
11. Allow players to restart the game using the Restart button.

## 🛠️ Technologies Used

- Python
- Tkinter library
- `tkinter.messagebox`

## 🧠 Concepts Used

- Functions
- Global variables
- Lists and Nested Lists
- 2D Arrays (Game Board)
- `for` loops
- `if-else` statements
- Lambda functions
- Button commands and event handling
- GUI development
- Grid layout management
- Conditional logic
- Window positioning and geometry

## ▶️ How to Run

1. Save the program as `tic_tac_toe.py`.
2. Make sure Python is installed on your system.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python tic_tac_toe.py
```

5. The Tic Tac Toe game window will open. Start playing!

---

**Part of my 12 Weeks → 12+ Projects challenge.** 🚀