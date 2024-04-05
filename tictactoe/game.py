# tictactoe/game.py

from .ai import TicTacToeAI

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.ai = TicTacToeAI(self.board, 'X')
        self.current_player = 'O'  # Let's assume the human player is 'O' and goes first

    def print_board(self):
        for row in self.board:
            print('|'.join([cell if cell != '' else ' ' for cell in row]))
            print('-' * 5)

    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'O'

    def user_move(self):
        valid_move = False
        while not valid_move:
            user_input = input("Enter your move as row,col (0-based index): ")
            try:
                row, col = map(int, user_input.split(','))
                if self.board[row][col] == '':
                    self.board[row][col] = self.current_player
                    valid_move = True
                else:
                    print("That space is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Try again using row,col format with 0, 1, or 2.")

    def play(self):
        while not self.ai.is_winner('X') and not self.ai.is_winner('O') and not self.ai.is_board_full():
            self.print_board()
            if self.current_player == 'O':  # Human turn
                self.user_move()
            else:
                print("AI is making a move...")
                move = self.ai.find_best_move()
                self.ai.make_move(move, self.current_player)

            if self.ai.is_winner(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return

            if self.ai.is_board_full():
                self.print_board()
                print("It's a draw!")
                return

            self.switch_player()

        self.print_board()
        if self.ai.is_winner('X'):
            print("AI wins!")
        elif self.ai.is_winner('O'):
            print("You win!")
        else:
            print("It's a draw!")


# Assuming the AI class has been defined above with necessary methods implemented:
game = TicTacToe()
game.play()
