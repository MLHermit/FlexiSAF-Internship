# Tic Tac Toe AI

This project simulates a simple AI agent that plays the game of Tic Tac Toe. The AI agent uses basic strategies to choose its moves and can learn from the outcomes of the games it plays.

## Project Structure

```
tic_tac_toe_ai
├── src
│   ├── agent.py       # Defines the AI agent that plays Tic Tac Toe
│   ├── board.py       # Manages the state of the Tic Tac Toe board
│   ├── game.py        # Implements the main game logic
│   └── main.py        # Entry point for the program
├── requirements.txt    # Lists the dependencies required for the project
└── README.md           # Documentation for the project
```

## Game Rules

Tic Tac Toe is a two-player game where players take turns marking a square on a 3x3 grid. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. If all squares are filled and no player has three in a row, the game ends in a tie.

## Running the Program

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
4. Run the main program:
   ```
   python src/main.py
   ```

## AI Functionality

The AI agent is designed to make strategic moves based on the current state of the board. It can choose the best move to either win the game or block the opponent from winning. The agent can also learn from its experiences to improve its strategy over time.