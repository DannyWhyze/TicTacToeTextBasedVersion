"""
Player classes for Tic-Tac-Toe game
"""
import random
from ui_utils import print_info

class Player:
    """
    Base class for all player types in the game.
    """
    
    def __init__(self, symbol, name="Player"):
        """
        Initialize a player.
        
        Args:
            symbol: The player's symbol (X or O)
            name: The player's name
        """
        self.symbol = symbol
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        
    def get_move(self, board):
        """
        Get the player's next move.
        Must be implemented by subclasses.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        raise NotImplementedError("Subclasses must implement get_move()")
        
    def update_stats(self, result):
        """
        Update player statistics.
        
        Args:
            result: "win", "loss", or "draw"
        """
        if result == "win":
            self.wins += 1
        elif result == "loss":
            self.losses += 1
        else:  # Draw
            self.draws += 1
            
    def display_stats(self):
        """Display the player's statistics."""
        print(f"{self.name} stats: Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}")


class HumanPlayer(Player):
    """
    Human player that gets moves from user input.
    """
    
    def get_move(self, board):
        """
        Get move from human player via console input.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        max_attempts = 5
        attempts = 0
        
        print_info(f"{self.name}'s turn!")
        
        while attempts < max_attempts:
            try:
                move_str = input("Enter a number between 1-9: ").strip()
                
                if not move_str:
                    print("No input detected. Please enter a number between 1 and 9.")
                    attempts += 1
                    continue
                
                try:
                    move = int(move_str)
                except ValueError:
                    print("Invalid input! Please enter a number.")
                    attempts += 1
                    continue
                
                if move < 1 or move > 9:
                    print("Invalid input! Please enter a number between 1 and 9.")
                    attempts += 1
                    continue
                
                # Get position from move number
                if move not in board.positions:
                    print("Invalid position! Please enter a number between 1 and 9.")
                    attempts += 1
                    continue
                
                row, col = board.positions[move]
                
                if not board.is_valid_move(row, col):
                    print("This position is already taken! Choose another one.")
                    attempts += 1
                    continue
                
                return row, col
                
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                attempts += 1
                print(f"Please try again. {max_attempts - attempts} attempts remaining.")
        
        print("Too many invalid attempts. Please try one more time carefully.")
        while True:
            try:
                move = int(input("Enter a number between 1-9 (for an empty position): "))
                if 1 <= move <= 9:
                    row, col = board.positions[move]
                    if board.is_valid_move(row, col):
                        return row, col
                    else:
                        print("Position already taken. Try another one.")
                else:
                    print("Invalid number. Please enter 1-9.")
            except ValueError:
                print("Please enter a valid number.")


class ComputerPlayer(Player):
    """
    Computer player with different difficulty levels.
    """
    
    def __init__(self, symbol, difficulty=1, name="Computer"):
        """
        Initialize computer player.
        
        Args:
            symbol: The computer's symbol
            difficulty: 1=Easy, 2=Medium, 3=Hard
            name: The computer's name
        """
        super().__init__(symbol, name)
        self.difficulty = difficulty
        
    def get_move(self, board):
        """
        Get the computer's move based on the difficulty level.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        print_info(f"{self.name}'s turn (thinking...)")
        
        if self.difficulty == 1:
            return self._get_easy_move(board)
        elif self.difficulty == 2:
            return self._get_medium_move(board)
        else:  # difficulty == 3
            return self._get_hard_move(board)
            
    def _get_easy_move(self, board):
        """
        Easy difficulty: Make a random move.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        empty_positions = board.get_empty_positions()
        
        if empty_positions:
            return random.choice(empty_positions)
        return None  # This should not happen unless the board is full
        
    def _get_medium_move(self, board):
        """
        Medium difficulty: Try to win or block opponent from winning.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        opponent_symbol = board.PLAYER_X if self.symbol == board.PLAYER_O else board.PLAYER_O
        
        # First, check if computer can win in the next move
        for row, col in board.get_empty_positions():
            board_copy = board.get_copy()
            board_copy.make_move(row, col, self.symbol)
            
            if board_copy.check_winner() == self.symbol:
                return row, col
                
        # Next, check if opponent can win in the next move and block it
        for row, col in board.get_empty_positions():
            board_copy = board.get_copy()
            board_copy.make_move(row, col, opponent_symbol)
            
            if board_copy.check_winner() == opponent_symbol:
                return row, col
                
        # If no winning moves, prefer center
        if board.is_valid_move(1, 1):
            return 1, 1
            
        # Then prefer corners
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        empty_corners = [pos for pos in corners if board.is_valid_move(pos[0], pos[1])]
        
        if empty_corners:
            return random.choice(empty_corners)
            
        # Otherwise make a random move
        return self._get_easy_move(board)
        
    def _get_hard_move(self, board):
        """
        Hard difficulty: Use minimax algorithm to find optimal move.
        
        Args:
            board: The current game board
            
        Returns:
            tuple: (row, col) position of the move
        """
        # Check if center is available (often a good first move)
        if board.is_valid_move(1, 1):
            return 1, 1
            
        opponent_symbol = board.PLAYER_X if self.symbol == board.PLAYER_O else board.PLAYER_O
        
        best_score = float('-inf')
        best_move = None
        
        # Try all possible moves and evaluate them
        for row, col in board.get_empty_positions():
            board_copy = board.get_copy()
            board_copy.make_move(row, col, self.symbol)
            
            # Use minimax to evaluate this move
            score = self._minimax(board_copy, 0, False, self.symbol, opponent_symbol)
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
                
        return best_move if best_move else self._get_easy_move(board)
        
    def _minimax(self, board, depth, is_maximizing, comp_symbol, player_symbol, alpha=float('-inf'), beta=float('inf')):
        """
        Minimax algorithm with alpha-beta pruning for optimal move finding.
        
        Args:
            board: Current board state
            depth: Current search depth
            is_maximizing: True if maximizing player's turn
            comp_symbol: Computer's symbol
            player_symbol: Player's symbol
            alpha: Alpha value for pruning
            beta: Beta value for pruning
            
        Returns:
            int: Score of the current board state
        """
        # Check terminal states
        winner = board.check_winner()
        
        if winner == comp_symbol:
            return 10 - depth  # Computer wins
        elif winner == player_symbol:
            return depth - 10  # Player wins
        elif board.is_full():
            return 0  # Draw
            
        if is_maximizing:
            # Computer's turn
            best_score = float('-inf')
            
            for row, col in board.get_empty_positions():
                board_copy = board.get_copy()
                board_copy.make_move(row, col, comp_symbol)
                
                score = self._minimax(
                    board_copy, depth + 1, False, 
                    comp_symbol, player_symbol, alpha, beta
                )
                
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break
                    
            return best_score
        else:
            # Player's turn
            best_score = float('inf')
            
            for row, col in board.get_empty_positions():
                board_copy = board.get_copy()
                board_copy.make_move(row, col, player_symbol)
                
                score = self._minimax(
                    board_copy, depth + 1, True, 
                    comp_symbol, player_symbol, alpha, beta
                )
                
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break
                    
            return best_score