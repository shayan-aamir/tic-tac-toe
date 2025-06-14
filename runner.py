"""
Tic Tac Toe game runner with graphical interface.
"""

import tkinter as tk
from tkinter import messagebox
import tictactoe as ttt

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = ttt
        self.board = self.game.initial_state()
        self.buttons = []
        
        # Create game board
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
        
        # Create reset button
        reset_button = tk.Button(
            root,
            text="Reset Game",
            font=('Arial', 12),
            command=self.reset_game
        )
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Start with AI move if it's O's turn
        if self.game.player(self.board) == self.game.O:
            self.make_ai_move()

    def make_move(self, row, col):
        """Handle player's move and AI's response."""
        if self.game.terminal(self.board):
            return
            
        if self.game.player(self.board) == self.game.X:
            action = (row, col)
            if action in self.game.actions(self.board):
                self.board = self.game.result(self.board, action)
                self.update_board()
                
                if not self.game.terminal(self.board):
                    self.make_ai_move()

    def make_ai_move(self):
        """Make AI's move using minimax algorithm."""
        if self.game.terminal(self.board):
            return
            
        action = self.game.minimax(self.board)
        if action is not None:
            self.board = self.game.result(self.board, action)
            self.update_board()
            
            # Check for game end
            if self.game.terminal(self.board):
                self.check_game_end()

    def update_board(self):
        """Update the GUI to reflect the current board state."""
        for i in range(3):
            for j in range(3):
                button = self.buttons[i * 3 + j]
                if self.board[i][j] == self.game.X:
                    button.config(text="X", state="disabled")
                elif self.board[i][j] == self.game.O:
                    button.config(text="O", state="disabled")
                else:
                    button.config(text="", state="normal")

    def check_game_end(self):
        """Check if the game has ended and show appropriate message."""
        if self.game.terminal(self.board):
            winner = self.game.winner(self.board)
            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            else:
                messagebox.showinfo("Game Over", "It's a tie!")

    def reset_game(self):
        """Reset the game to initial state."""
        self.board = self.game.initial_state()
        for button in self.buttons:
            button.config(text="", state="normal")
        
        # Start with AI move if it's O's turn
        if self.game.player(self.board) == self.game.O:
            self.make_ai_move()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop() 