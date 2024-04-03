# tictactoe/game.py

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_turn = 'X'

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_turn
            return True
        return False

    def is_valid_move(self, row, col):
        return self.board[row][col] == ''

    def toggle_turn(self):
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        lines = self.board + list(zip(*self.board))  # rows and columns
        lines.extend([
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # diagonal top-left to bottom-right
            [self.board[0][2], self.board[1][1], self.board[2][0]]   # diagonal top-right to bottom-left
        ])
        for line in lines:
            if line.count(line[0]) == 3 and line[0] != '':
                return line[0]
        return None

    def check_draw(self):
        return all(cell != '' for row in self.board for cell in row)

