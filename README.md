# Tic-Tac-Toe Game (Text-Based Version)

A Python-based Tic-Tac-Toe game with support for various game modes and difficulty levels. This project was developed using an object-oriented programming (OOP) approach to create a robust, maintainable, and extensible codebase for the classic game.

## Features

- **Game Modes**:
  - Human vs. Computer
  - Human vs. Human
- **Computer Difficulty Levels**:
  1. **Easy**: Random moves
  2. **Medium**: Blocks the player's winning moves
  3. **Hard**: Optimal strategy using the Minimax algorithm with Alpha-Beta pruning
- **Colorful Console Output**: Colored symbols and messages for an enhanced user experience
- **Statistics**: Tracks wins, losses, and draws for each player
- **Documentation**: Detailed documentation available in both English and German
- **Modular Design**: Clear separation of responsibilities across multiple modules

## Documentation
English: tic_tac_toe_documentation.html
German: tic_tac_toe_dokumentation.html

# Installation
Install Python: Ensure Python 3.10 or higher is installed.

# Clone the Repository

git clone https://github.com/DannyWhyze/TicTacToeTextBasedVersion.git
cd TicTacToeTextBasedVersion

# Create a Virtual Environment (optional)

python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows

# Install Dependencies

pip install -r requirements.txt

# Usage

## Object-Oriented Version
Start the game with python main_oop.py

## Procedural Version
python old_procedual_version/main.py

# Project Structure

```plaintext
TicTacToeTextBasedVersion/
│
├── [ascii_art.py](http://_vscodecontentref_/0)          # ASCII art for the game title banner
├── [ui_utils.py](http://_vscodecontentref_/1)           # Utility functions for the user interface (colored output)
├── [board.py](http://_vscodecontentref_/2)                 # Board class with game logic
├── [player.py](http://_vscodecontentref_/3)               # Player classes (human and computer)
├── [game.py](http://_vscodecontentref_/4)                   # Main game class that controls the game flow
├── [main_oop.py](http://_vscodecontentref_/5)           # Entry point for the OOP version
├── old_procedual_version/
│   ├── [coreLogic.py](http://_vscodecontentref_/6)      # Core logic for the procedural version
│   ├── [startGame.py](http://_vscodecontentref_/7)      # Game control for the procedural version
│   └── [main.py](http://_vscodecontentref_/8)                # Entry point for the procedural version
├── [reflection.html](http://_vscodecontentref_/9)                         # Project reflection (English)
├── [tic_tac_toe_documentation.html](http://_vscodecontentref_/10)  # Documentation (English)
├── [tic_tac_toe_dokumentation.html](http://_vscodecontentref_/11)  # Documentation (German)
├── [requirements.txt](http://_vscodecontentref_/12)                       # Dependencies (no external libraries required)
└── .gitignore                                                   # Ignored files for Git
