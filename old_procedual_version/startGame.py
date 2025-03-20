# Zu Beginn der Datei startGame.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dann deine normalen Imports
from old_procedual_version.coreLogic import *
from ui_utils import print_info, print_success, print_warning, print_error, colored_text, Colors

def setup_game():
    """
    Sets up the game by initializing the board and choosing game options.
    Returns a tuple containing (board, player_symbol, computer_symbol, difficulty, vs_computer, player_turn)
    """
    # Choose game mode
    vs_computer = choose_game_mode()
    
    # Variables for player symbols
    player1_symbol = None
    player2_symbol = None
    difficulty = None
    
    if vs_computer:
        # Choose difficulty level when playing against computer
        difficulty = choose_difficulty()
        # Choose symbol
        player1_symbol, player2_symbol = choose_symbol()
    else:
        # Playing against another human
        print("\nPlayer 1 will choose the symbol.")
        player1_symbol, player2_symbol = choose_symbol()
        print(f"Player 1 will use {player1_symbol}")
        print(f"Player 2 will use {player2_symbol}")
    
    # Determine who goes first
    if vs_computer:
        player_turn = determine_first_player()
    else:
        # For human vs human, player 1 always goes first
        player_turn = True
        print("\nPlayer 1 goes first!")
    
    # Create a new game board
    board = initialize_board()
    
    return board, player1_symbol, player2_symbol, difficulty, vs_computer, player_turn

def handle_player_move(board, player_symbol, is_player1=True, vs_computer=True):
    """
    Handles a player's move including input validation and board update.
    Returns the updated board.
    """
    # Display appropriate prompt
    if vs_computer:
        print("Your turn!")
    else:
        print(f"Player {1 if is_player1 else 2}'s turn!")
    
    print()
    
    # Get valid move from player
    row, col = validate_move(board)
    
    # Update the board
    board = make_move(board, row, col, player_symbol)
    print()
    
    # Display updated board
    display_board(board)
    
    return board

def handle_computer_move(board, computer_symbol, player_symbol, difficulty):
    """
    Handles the computer's move based on the selected difficulty.
    Returns the updated board.
    """
    print("\nComputer's turn!")
    
    # Get computer's move
    row, col = computer_move(board, difficulty, player_symbol, computer_symbol)
    
    # Update the board
    board = make_move(board, row, col, computer_symbol)
    print(f"Computer places at position {row+1},{col+1}")
    print()
    
    # Display updated board
    display_board(board)
    
    return board

def check_game_result(board, current_symbol, is_player1=True, vs_computer=True):
    """
    Checks if the game has ended (win or draw).
    Returns a tuple (is_game_over, result_message)
    """
    # Check for winner
    winner = check_winner(board)
    if winner:
        if vs_computer:
            if winner == current_symbol:
                return True, "Congratulations! You won! 🏆"  # Will be colored green by caller
            else:
                return True, "Computer won! Better luck next time. 😞"  # Will be colored red by caller
        else:
            if is_player1:
                return True, "Player 1 wins! 🏆"  # Will be colored green by caller
            else:
                return True, "Player 2 wins! 🏆"  # Will be colored green by caller
    
    # Check for draw
    if is_board_full(board):
        return True, "It's a draw! The board is full. 🤝"  # Will be colored yellow by caller
    
    # Game continues
    return False, ""

def play_game():
    """
    Main game function that controls the game flow.
    """
    # Setup game
    print_info("\n=== NEW GAME ===")
    board, player1_symbol, player2_symbol, difficulty, vs_computer, player_turn = setup_game()
    
    # Display initial board
    display_board(board)
    
    # Main game loop
    game_active = True
    while game_active:
        if player_turn:
            # Player 1's move
            board = handle_player_move(board, player1_symbol, True, vs_computer)
            
            # Check result after player 1's move
            game_over, message = check_game_result(board, player1_symbol, True, vs_computer)
            if game_over:
                if "won" in message and "Computer" not in message:
                    print_success(message)
                elif "draw" in message:
                    print_warning(message)
                else:
                    print_error(message)
                game_active = False
                break
        else:
            # Player 2's or Computer's move
            if vs_computer:
                board = handle_computer_move(board, player2_symbol, player1_symbol, difficulty)
            else:
                board = handle_player_move(board, player2_symbol, False, vs_computer)
            
            # Check result after player 2's or computer's move
            game_over, message = check_game_result(board, player2_symbol, False, vs_computer)
            if game_over:
                if "won" in message and "Computer" not in message:
                    print_success(message)
                elif "draw" in message:
                    print_warning(message)
                else:
                    print_error(message)
                game_active = False
                break
        
        # Switch turns for next round
        player_turn = not player_turn