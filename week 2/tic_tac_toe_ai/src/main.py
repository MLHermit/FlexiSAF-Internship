# main.py

# This file serves as the entry point for the program. It initializes the game and starts the main game loop by creating instances of Board, TicTacToeAgent, and Game.

from board import Board
from agent import TicTacToeAgent
from game import Game

def main():
    board = Board()
    agent = TicTacToeAgent()
    game = Game(board, agent)
    
    game.play()

if __name__ == "__main__":
    main()