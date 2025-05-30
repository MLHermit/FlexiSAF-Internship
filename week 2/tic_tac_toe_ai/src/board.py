class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state

    def initialize(self):
        self.board = [' ' for _ in range(9)]  # Reset the board to empty

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]               # Diagonal
        ]
        for combination in winning_combinations:
            if all(self.board[i] == player for i in combination):
                return True
        return False

    def is_full(self):
        return ' ' not in self.board  # Check if the board is full