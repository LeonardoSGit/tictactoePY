# tictactoe/gui.py

import tkinter as tk
from .game import TicTacToe
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font='normal 20 bold', height=2, width=5,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col]['text'] = self.game.current_player
            if self.game.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.game.current_player} wins!")
                self.game.reset_board()
                self.clear_buttons()
                pass
            elif self.game.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game.reset_board()  
                self.clear_buttons()
                pass

    def clear_buttons(self):
        for row in range(len(self.buttons)):
            for col in range(len(self.buttons[row])):
                self.buttons[row][col]['text'] = ''

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()
