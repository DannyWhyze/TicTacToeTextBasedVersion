"""
Game class for Tic-Tac-Toe
"""
import random
from board import Board
from player import HumanPlayer, ComputerPlayer
from ui_utils import print_info, print_success, print_warning, print_error, Colors, colored_text

class TicTacToeGame:
    """
    Main game class that manages the game flow and state.
    """
    
    def __init__(self):
        """Initialize a new game instance."""
        self.board = None
        self.players = []
        self.current_player_index = 0
        self.vs_computer = True
        self.game_active = False
        
    def setup_game(self):
        """
        Set up a new game by initializing the board and players.
        """
        # Create a new board
        self.board = Board()
        
        # Choose game mode
        self.vs_computer = self._choose_game_mode()
        
        # Set up players
        if self.vs_computer:
            difficulty = self._choose_difficulty()
            player_symbol, computer_symbol = self._choose_symbol()
            
            self.players = [
                HumanPlayer(player_symbol, "Player"),
                ComputerPlayer(computer_symbol, difficulty, "Computer")
            ]
        else:
            # Human vs Human
            print_info("\nPlayer 1 will choose the symbol.")
            player1_symbol, player2_symbol = self._choose_symbol()
            
            self.players = [
                HumanPlayer(player1_symbol, "Player 1"),
                HumanPlayer(player2_symbol, "Player 2")
            ]
        
        # Determine who goes first
        self.current_player_index = 0 if self._determine_first_player() else 1
        
        # Display the initial board
        self.board.display()
        
        # Set game as active
        self.game_active = True
        
    def play(self):
        """
        Main game loop that handles the turns and checks for game end.
        """
        while self.game_active:
            # Get current player
            current_player = self.players[self.current_player_index]
            
            # Get and make move
            row, col = current_player.get_move(self.board)
            self.board.make_move(row, col, current_player.symbol)
            self.board.display()
            
            # Check for winner
            winner = self.board.check_winner()
            if winner:
                self._handle_winner(winner)
                break
                
            # Check for draw
            if self.board.is_full():
                self._handle_draw()
                break
                
            # Switch to next player
            self.current_player_index = (self.current_player_index + 1) % 2
            
    def _handle_winner(self, winner_symbol):
        """
        Handle the end of the game when there's a winner.
        
        Args:
            winner_symbol: Symbol of the winning player
        """
        # Get winner and loser
        winner = next(p for p in self.players if p.symbol == winner_symbol)
        loser = next(p for p in self.players if p.symbol != winner_symbol)
        
        # Update stats
        winner.update_stats("win")
        loser.update_stats("loss")
        
        # Display message
        if self.vs_computer:
            if isinstance(winner, HumanPlayer):
                print_success("Congratulations! You won! 🏆")
            else:
                print_error("Computer won! Better luck next time. 😞")
        else:
            print_success(f"{winner.name} wins! 🏆")
            
        self.game_active = False
        
    def _handle_draw(self):
        """Handle the end of the game when it's a draw."""
        print_warning("It's a draw! The board is full. 🤝")
        
        # Update stats for both players
        for player in self.players:
            player.update_stats("draw")
            
        self.game_active = False
        
    def _choose_game_mode(self):
        """
        Let the player choose the game mode.
        
        Returns:
            bool: True for vs Computer, False for vs Human
        """
        print_info("\nSelect game mode:")
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
                
    def _choose_difficulty(self):
        """
        Let the player choose the difficulty level when playing against computer.
        
        Returns:
            int: Difficulty level (1-3)
        """
        print_info("\nSelect difficulty level:")
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
                
    def _choose_symbol(self):
        """
        Let the player choose their symbol (X or O).
        
        Returns:
            tuple: (player_symbol, opponent_symbol)
        """
        max_attempts = 3
        
        for attempt in range(max_attempts):
            try:
                choice = input("Which symbol do you want to use? X or O: ").strip().upper()
                
                if choice == 'O':
                    print(f"You have chosen {self.board.PLAYER_O} as your symbol.")
                    print(f"The opponent will use {self.board.PLAYER_X}.")
                    return (self.board.PLAYER_O, self.board.PLAYER_X)
                elif choice == 'X':
                    print(f"You have chosen {self.board.PLAYER_X} as your symbol.")
                    print(f"The opponent will use {self.board.PLAYER_O}.")
                    return (self.board.PLAYER_X, self.board.PLAYER_O)
                else:
                    print(f"Invalid choice '{choice}'. Please enter either 'X' or 'O'.")
                    print(f"Attempts remaining: {max_attempts - attempt - 1}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print(f"Attempts remaining: {max_attempts - attempt - 1}")
        
        # Default choice if user makes too many invalid attempts
        print("Too many invalid attempts. Defaulting to X.")
        print(f"You will use {self.board.PLAYER_X} as your symbol.")
        print(f"The opponent will use {self.board.PLAYER_O}.")
        return (self.board.PLAYER_X, self.board.PLAYER_O)
        
    def _determine_first_player(self):
        """
        Determine which player goes first.
        For vs. computer mode, it's random. For vs. human mode, Player 1 goes first.
        
        Returns:
            bool: True if first player (or human) goes first, False otherwise
        """
        if self.vs_computer:
            player_first = random.choice([True, False])
            if player_first:
                print_info("\nYou go first!")
            else:
                print_info("\nComputer goes first!")
            return player_first
        else:
            print_info("\nPlayer 1 goes first!")
            return True
            
    def display_stats(self):
        """Display game statistics for all players."""
        print_info("\n--- Game Statistics ---")
        for player in self.players:
            player.display_stats()