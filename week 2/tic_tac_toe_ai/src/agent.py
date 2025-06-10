class TicTacToeAgent:
    def __init__(self):
        self.strategy = {}

    def choose_move(self, board):
        # Simple strategy: choose the first available move
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return (i, j)
        return None

    def learn(self, outcome):
        # Update strategy based on the outcome of the game
        pass  # Learning logic can be implemented here later