class Game:
    def __init__(self, board, agent):
        self.board = board
        self.agent = agent

    def play(self):
        while True:
            self.board.display()
            if self.board.is_full():
                print("It's a tie!")
                break
            
            # Player's turn
            move = int(input("Enter your move (1-9): ")) - 1
            if not self.board.make_move(move, 'X'):
                print("Invalid move. Try again.")
                continue
            
            if self.check_winner('X'):
                self.board.display()
                print("Player wins!")
                break
            
            # AI's turn
            ai_move = self.agent.choose_move(self.board)
            self.board.make_move(ai_move, 'O')
            if self.check_winner('O'):
                self.board.display()
                print("AI wins!")
                break

    def check_winner(self, player):
        return self.board.is_winner(player)