class TicTacToeAI:
    def __init__(self, board, ai_player):
        self.board = board
        self.ai_player = ai_player
        self.human_player = 'O' if ai_player == 'X' else 'X'

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check column
                return True
        
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False

    def is_board_full(self):
        # Return True if the board is full (a draw), False otherwise.
        return all(cell != '' for row in self.board for cell in row)

    def evaluate(self):
        # Evaluate the board from the AI's perspective.
        if self.is_winner(self.ai_player):
            return 1
        elif self.is_winner(self.human_player):
            return -1
        else:
            return 0

    def minimax(self, is_ai_turn):
        if self.is_winner(self.ai_player):
            return 1
        elif self.is_winner(self.human_player):
            return -1
        if self.is_board_full():
            return 0

        if is_ai_turn:
            best_val = -float('inf')
            for move in self.get_available_moves():
                # Make the move
                self.make_move(move, self.ai_player)
                value = self.minimax(False)
                # Undo the move
                self.undo_move(move)
                best_val = max(best_val, value)
            return best_val
        else:
            best_val = float('inf')
            for move in self.get_available_moves():
                # Make the move
                self.make_move(move, self.human_player)
                value = self.minimax(True)
                # Undo the move
                self.undo_move(move)
                best_val = min(best_val, value)
            return best_val


    def get_available_moves(self):
        # Return a list of available moves.
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '':
                    moves.append((row, col))
        return moves

    def make_move(self, move, player):
        # Make a move on the board.
        row, col = move
        if self.board[row][col] == '':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, move):
        # Undo a move on the board.
        row, col = move
        self.board[row][col] = ''

    def find_best_move(self):
        best_val = -float('inf')
        best_move = None
        for move in self.get_available_moves():
            self.make_move(move, self.ai_player)
            move_val = self.minimax(False)
            self.undo_move(move)
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move

    def play(self):
        move = self.find_best_move()
        self.make_move(move, self.ai_player)
