"""
Board class for Tic-Tac-Toe game
"""
from ui_utils import Colors, colored_text

class Board:
    """
    Represents the Tic-Tac-Toe game board.
    Handles board state, move validation, and winner detection.
    """
    
    def __init__(self, empty_symbol="⬜️", player_x_symbol="❌", player_o_symbol="⭕"):
        """
        Initialize a new board with empty cells.
        
        Args:
            empty_symbol: Symbol for empty cells
            player_x_symbol: Symbol for player X
            player_o_symbol: Symbol for player O
        """
        self.EMPTY = empty_symbol
        self.PLAYER_X = player_x_symbol
        self.PLAYER_O = player_o_symbol
        self.grid = self.initialize_grid()
        self.positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2)
        }
        
    def initialize_grid(self):
        """
        Initialize a fresh 3x3 grid filled with empty cells.
        """
        return [
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY],
            [self.EMPTY, self.EMPTY, self.EMPTY]
        ]
        
    def display(self):
        """
        Display the current board state with color-coded symbols.
        """
        position_labels = {
            (row, col): str(pos) 
            for pos, (row, col) in self.positions.items()
        }
        
        print("\n  Current Board:")
        print("  -------------")
        
        for i in range(3):
            print("  |", end=" ")
            for j in range(3):
                cell = self.grid[i][j]
                if cell == self.EMPTY:
                    print(colored_text(position_labels[(i, j)], Colors.BLUE), end=" | ")
                elif cell == self.PLAYER_X:
                    print(colored_text("X", Colors.RED), end=" | ")
                else:  # cell == self.PLAYER_O
                    print(colored_text("O", Colors.GREEN), end=" | ")
            print("\n  -------------")
        print()
        
    def make_move(self, row, col, symbol):
        """
        Place a symbol at the specified position on the grid.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            symbol: Symbol to place (PLAYER_X or PLAYER_O)
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        if not self.is_valid_move(row, col):
            return False
            
        self.grid[row][col] = symbol
        return True
        
    def is_valid_move(self, row, col):
        """
        Check if a move is valid (cell is empty and within bounds).
        
        Args:
            row: Row index
            col: Column index
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
            
        return self.grid[row][col] == self.EMPTY
        
    def get_empty_positions(self):
        """
        Get all empty positions on the board.
        
        Returns:
            list: List of (row, col) tuples for all empty cells
        """
        empty_positions = []
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == self.EMPTY:
                    empty_positions.append((row, col))
        return empty_positions
        
    def is_full(self):
        """
        Check if the board is full (no empty cells).
        
        Returns:
            bool: True if board is full, False otherwise
        """
        return len(self.get_empty_positions()) == 0
        
    def check_winner(self):
        """
        Check if there is a winner on the board.
        
        Returns:
            Symbol of the winner (PLAYER_X or PLAYER_O) or None if no winner
        """
        # Check rows
        for row in range(3):
            if (self.grid[row][0] != self.EMPTY and 
                self.grid[row][0] == self.grid[row][1] == self.grid[row][2]):
                return self.grid[row][0]
                
        # Check columns
        for col in range(3):
            if (self.grid[0][col] != self.EMPTY and
                self.grid[0][col] == self.grid[1][col] == self.grid[2][col]):
                return self.grid[0][col]
                
        # Check diagonals
        if (self.grid[0][0] != self.EMPTY and 
            self.grid[0][0] == self.grid[1][1] == self.grid[2][2]):
            return self.grid[0][0]
            
        if (self.grid[0][2] != self.EMPTY and 
            self.grid[0][2] == self.grid[1][1] == self.grid[2][0]):
            return self.grid[0][2]
            
        # No winner
        return None
        
    def get_copy(self):
        """
        Create a deep copy of the current board state.
        
        Returns:
            Board: A new Board object with the same state
        """
        new_board = Board(self.EMPTY, self.PLAYER_X, self.PLAYER_O)
        for i in range(3):
            for j in range(3):
                new_board.grid[i][j] = self.grid[i][j]
        return new_board
        
    def reset(self):
        """Reset the board to its initial empty state."""
        self.grid = self.initialize_grid()