# Tic Tac Toe with AI

A Python implementation of Tic Tac Toe with an unbeatable AI opponent using the minimax algorithm. The game features a graphical user interface built with tkinter.

## Features

- Classic 3x3 Tic Tac Toe gameplay
- Unbeatable AI opponent using the minimax algorithm
- Clean and intuitive graphical user interface
- Game state tracking and win detection
- Option to reset the game at any time
- Support for both player vs AI gameplay

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tictactoe-ai.git
cd tictactoe-ai
```

2. No additional packages are required as the project only uses Python's standard library.

## How to Play

1. Run the game:
```bash
python runner.py
```

2. Game Rules:
   - You play as X (the first player)
   - The AI plays as O (the second player)
   - Click on any empty cell to make your move
   - The AI will automatically respond with its move
   - The game ends when either:
     - A player gets three in a row (horizontally, vertically, or diagonally)
     - All cells are filled (resulting in a tie)

3. Controls:
   - Click any empty cell to make your move
   - Use the "Reset Game" button to start a new game
   - Close the window to exit the game

## Technical Details

The project consists of two main files:

1. `tictactoe.py`: Contains the core game logic and AI implementation
   - Implements the minimax algorithm for optimal AI moves
   - Handles game state management
   - Provides functions for move validation and win detection

2. `runner.py`: Implements the graphical user interface
   - Creates a 3x3 grid of buttons for the game board
   - Manages user input and AI responses
   - Displays game status and results
   - Provides game reset functionality

## AI Implementation

The AI uses the minimax algorithm to determine the optimal move in any given situation. This algorithm:
- Evaluates all possible moves and their outcomes
- Assumes both players play optimally
- Always chooses the move that leads to the best possible outcome
- Makes the AI unbeatable (the best possible outcome for a human player is a tie)

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch for your feature
3. Making your changes
4. Submitting a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- The minimax algorithm implementation is based on the classic game theory approach
- The GUI is built using Python's tkinter library
- Inspired by the classic game of Tic Tac Toe 
