# tictactoe/game.py

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # X always goes first

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        
    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.toggle_player()  # After a move, switch to the other player
            return True
        return False

    def is_valid_move(self, row, col):
        return self.board[row][col] == ''

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

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
