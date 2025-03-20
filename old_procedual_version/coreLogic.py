"""
Core Logic for Tic-Tac-Toe Game

This module contains the core game mechanics including:
- Board initialization and display
- Player and computer move logic
- Game state validation
- AI opponents with varying difficulties

The module implements three difficulty levels:
1. Easy: Random moves
2. Medium: Strategic blocking
3. Hard: Minimax algorithm with Alpha-Beta pruning
"""

import random
from ui_utils import Colors, colored_text

EMPTY = "⬜️"     # Symbol used for an empty cell
PLAYER_X = "❌"  # Symbol for player X
PLAYER_O = "⭕"  # Symbol for player O

def display_board(board):
    """
    Prints the board in a user-friendly layout with colors and position numbers.
    """
    # Position reference map for empty cells
    positions = {
        (0, 0): "1", (0, 1): "2", (0, 2): "3",
        (1, 0): "4", (1, 1): "5", (1, 2): "6",
        (2, 0): "7", (2, 1): "8", (2, 2): "9"
    }
    
    print("\n  Current Board:")
    print("  -------------")
    
    for i in range(3):
        print("  |", end=" ")
        for j in range(3):
            cell = board[i][j]
            if cell == EMPTY:
                # Show position number for empty cells
                print(colored_text(positions[(i, j)], Colors.BLUE), end=" | ")
            elif cell == PLAYER_X:
                # Show X in red
                print(colored_text("X", Colors.RED), end=" | ")
            else:  # cell == PLAYER_O
                # Show O in green
                print(colored_text("O", Colors.GREEN), end=" | ")
        print("\n  -------------")
    print()
    
def initialize_board():
    """
    Returns a new 3x3 board filled with the EMPTY symbol.
    """
    return [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    
def choose_symbol():
    """
    Asks the player which symbol they want to use ('X' or 'O').
    Returns a tuple (playerSymbol, opponentSymbol).
    """
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            choice = input("Which symbol do you want to use? X or O: ").strip().upper()
            
            if choice == 'O':
                print(f"You have chosen {PLAYER_O} as your symbol.")
                print(f"The opponent will use {PLAYER_X}.")
                return (PLAYER_O, PLAYER_X)
            elif choice == 'X':
                print(f"You have chosen {PLAYER_X} as your symbol.")
                print(f"The opponent will use {PLAYER_O}.")
                return (PLAYER_X, PLAYER_O)
            else:
                print(f"Invalid choice '{choice}'. Please enter either 'X' or 'O'.")
                print(f"Attempts remaining: {max_attempts - attempt - 1}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print(f"Attempts remaining: {max_attempts - attempt - 1}")
    
    # Default choice if user makes too many invalid attempts
    print("Too many invalid attempts. Defaulting to X.")
    print(f"You will use {PLAYER_X} as your symbol.")
    print(f"The opponent will use {PLAYER_O}.")
    return (PLAYER_X, PLAYER_O)

def determine_first_player():
    """
    Randomly determines who goes first: player or computer.
    Returns True if player goes first, False if computer goes first.
    """
    player_first = random.choice([True, False])
    if player_first:
        print()
        print("You go first!")
    else:
        print()
        print("Computer goes first!")
        print()
    return player_first

def validate_move(board):
    """
    Validates player's move input (numbers 1-9).
    Returns row and column indices (0-2, 0-2) if the move is valid.
    """
    # Mapping of numbers 1-9 to board positions (row, col)
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        try:
            move = input("Enter a number between 1-9: ").strip()
            
            # Check for empty input
            if not move:
                print("No input detected. Please enter a number between 1 and 9.")
                attempts += 1
                continue
            
            # Try to convert to integer
            try:
                move = int(move)
            except ValueError:
                print("Invalid input! Please enter a number.")
                attempts += 1
                continue
                
            # Check range
            if move < 1 or move > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
                attempts += 1
                continue
                
            row, col = positions[move]
            
            # Check if the position is empty
            if board[row][col] != EMPTY:
                print("This position is already taken! Choose another one.")
                attempts += 1
                continue
                
            return row, col
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            attempts += 1
            print(f"Please try again. {max_attempts - attempts} attempts remaining.")
    
    # CHANGE THIS: Instead of using a random move, ask again
    print("Too many invalid attempts. Please try one more time carefully.")
    while True:
        try:
            move = input("Enter a number between 1-9 (for an empty position): ").strip()
            move = int(move)
            if 1 <= move <= 9:
                row, col = positions[move]
                if board[row][col] == EMPTY:
                    return row, col
                else:
                    print("Position already taken. Try another one.")
            else:
                print("Invalid number. Please enter 1-9.")
        except ValueError:
            print("Please enter a valid number.")

def make_move(board, row, col, symbol):
    """
    Places the player's or computer's symbol on the board at the specified position.
    """
    board[row][col] = symbol
    return board

def check_winner(board):
    """
    Checks if there is a winner on the board.
    Returns the winning symbol (PLAYER_X or PLAYER_O) or None if no winner.
    """
    try:
        # Validate board structure
        if not isinstance(board, list) or len(board) != 3:
            print("Warning: Invalid board structure in check_winner.")
            return None
            
        for row in board:
            if not isinstance(row, list) or len(row) != 3:
                print("Warning: Invalid row structure in check_winner.")
                return None
        
        # Check rows
        for row in range(3):
            if board[row][0] != EMPTY and board[row][0] == board[row][1] == board[row][2]:
                return board[row][0]
        
        # Check columns
        for col in range(3):
            if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        
        # Check diagonals
        if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
    except Exception as e:
        print(f"Error checking winner: {str(e)}")
    
    # No winner
    return None

def is_board_full(board):
    """
    Checks if the board is full (no empty cells left).
    Returns True if the board is full, False otherwise.
    """
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    return True

def choose_difficulty():
    """
    Allows the player to choose a difficulty level.
    Returns an integer representing the difficulty (1=Easy, 2=Medium, 3=Hard).
    """
    print("\nSelect difficulty level:")
    print("1. Easy (Random moves)")
    print("2. Medium (Blocks winning moves)")
    print("3. Hard (Optimal strategy)")
    
    while True:
        try:
            difficulty = int(input("Enter difficulty (1-3): ").strip())
            if 1 <= difficulty <= 3:
                return difficulty
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board, difficulty=1, player_symbol=None, computer_symbol=None):
    """
    Computer selects a position on the board based on the difficulty level.
    Returns the row and column indices of the chosen position.
    
    difficulty: 1=Easy, 2=Medium, 3=Hard
    player_symbol: Required for Medium and Hard difficulties
    computer_symbol: Required for Hard difficulty
    """
    if difficulty == 1:
        return computer_move_easy(board)
    elif difficulty == 2:
        return computer_move_medium(board, player_symbol)
    else:  # difficulty == 3
        return computer_move_hard(board, computer_symbol, player_symbol)

def computer_move_easy(board):
    """
    Easy difficulty: Computer selects a random valid position.
    """
    # Get all empty positions
    empty_positions = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                empty_positions.append((row, col))
    
    # Randomly select one of the empty positions
    if empty_positions:
        return random.choice(empty_positions)
    return None  # This should not happen unless the board is full

def computer_move_medium(board, player_symbol):
    """
    Medium difficulty: Computer blocks player's winning moves or makes winning moves when possible.
    If no winning opportunity exists, makes a random move.
    """
    # First check if computer can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                # Try this position and see if computer would win
                board_copy = [row[:] for row in board]  # Create a deep copy to avoid modifying original
                board_copy[row][col] = PLAYER_X if player_symbol == PLAYER_O else PLAYER_O
                
                # If this move results in a win, choose it
                if check_winner(board_copy) == (PLAYER_X if player_symbol == PLAYER_O else PLAYER_O):
                    return row, col
    
    # Next, check if player could win in their next move and block it
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                # Try this position and see if player would win
                board_copy = [row[:] for row in board]  # Create a deep copy
                board_copy[row][col] = player_symbol
                
                # If this move would let player win, block it
                if check_winner(board_copy) == player_symbol:
                    return row, col
    
    # If no winning move to make or block, prefer center position
    if board[1][1] == EMPTY:
        return 1, 1
        
    # If center is taken, prefer corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    empty_corners = [corner for corner in corners if board[corner[0]][corner[1]] == EMPTY]
    if empty_corners:
        return random.choice(empty_corners)
    
    # Otherwise, make a random move (all remaining positions are edges)
    return computer_move_easy(board)

def computer_move_hard(board, computer_symbol, player_symbol):
    """
    Hard difficulty: Computer uses minimax algorithm with alpha-beta pruning to find optimal move.
    """
    # Check if center is available - often a good first move
    if board[1][1] == EMPTY:
        return 1, 1
    
    best_score = float('-inf')
    best_move = None
    
    # Evaluate all possible moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                # Try this position
                board_copy = [row[:] for row in board]
                board_copy[row][col] = computer_symbol
                
                # Use minimax to evaluate this move
                score = minimax(board_copy, 0, False, computer_symbol, player_symbol)
                
                # Update best move if this one is better
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    
    return best_move if best_move else computer_move_easy(board)

def minimax(board, depth, is_maximizing, computer_symbol, player_symbol, alpha=float('-inf'), beta=float('inf')):
    """
    Implementation of the minimax algorithm with alpha-beta pruning.
    
    The algorithm recursively evaluates all possible future board states to find
    the optimal move for the computer. Alpha-beta pruning is used to reduce the
    number of evaluated states by skipping branches that won't affect the final decision.
    
    Args:
        board: Current game board state (3x3 nested list)
        depth: Current recursion depth (starts at 0)
        is_maximizing: True if maximizing player's turn (computer), False otherwise
        computer_symbol: Symbol used by the computer (PLAYER_X or PLAYER_O)
        player_symbol: Symbol used by the human player
        alpha: Best score for maximizer found so far
        beta: Best score for minimizer found so far
    
    Returns:
        int: Score of the best move (-10 to +10)
            +10: Computer wins
            -10: Player wins
            0: Draw
            Scores are adjusted by depth to prefer quicker wins/longer losses
    
    Algorithm overview:
    1. Check terminal states (win, loss, draw)
    2. For maximizing player (computer):
       - Find highest score from all possible moves
       - Update alpha and prune branches where beta <= alpha
    3. For minimizing player (human):
       - Find lowest score from all possible moves
       - Update beta and prune branches where beta <= alpha
    """
    # Base case: check terminal states
    winner = check_winner(board)
    if winner == computer_symbol:
        return 10 - depth  # Win, prefer quicker wins
    elif winner == player_symbol:
        return depth - 10  # Loss, prefer longer games before losing
    elif is_board_full(board):
        return 0  # Draw
    
    if is_maximizing:
        # Computer's turn - maximize score
        best_score = float('-inf')
        
        # Try all possible moves
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    # Make the move
                    board_copy = [row[:] for row in board]
                    board_copy[row][col] = computer_symbol
                    
                    # Recursively evaluate this move (opponent's turn next)
                    score = minimax(board_copy, depth + 1, False, 
                                   computer_symbol, player_symbol, alpha, beta)
                    
                    # Update best score
                    best_score = max(score, best_score)
                    
                    # Update alpha for pruning
                    alpha = max(alpha, best_score)
                    
                    # Alpha-beta pruning
                    if beta <= alpha:
                        # This branch won't affect the decision at a higher level
                        break  # Beta cutoff
        
        return best_score
    else:
        # Player's turn - minimize score
        best_score = float('inf')
        
        # Try all possible moves
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    # Make the move
                    board_copy = [row[:] for row in board]
                    board_copy[row][col] = player_symbol
                    
                    # Recursively evaluate this move (computer's turn next)
                    score = minimax(board_copy, depth + 1, True, 
                                   computer_symbol, player_symbol, alpha, beta)
                    
                    # Update best score
                    best_score = min(score, best_score)
                    
                    # Update beta for pruning
                    beta = min(beta, best_score)
                    
                    # Alpha-beta pruning
                    if beta <= alpha:
                        # This branch won't affect the decision at a higher level
                        break  # Alpha cutoff
        
        return best_score

def choose_game_mode():
    """
    Allows the player to choose between playing against computer or another human.
    Returns True for computer opponent, False for human opponent.
    """
    print("\nSelect game mode:")
    print("1. Play against Computer")
    print("2. Play against Human")
    
    while True:
        try:
            mode = int(input("Enter mode (1-2): ").strip())
            if mode == 1:
                return True  # Computer opponent
            elif mode == 2:
                return False  # Human opponent
            else:
                print("Invalid choice. Please enter either 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    More detailed explanation if needed.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
    
    Returns:
        Description of what is returned
    
    Raises: (if applicable)
        ExceptionType: When and why this exception might be raised
    """
    # function implementation
