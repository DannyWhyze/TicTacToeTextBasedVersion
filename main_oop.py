"""
Main module for the Tic-Tac-Toe game (Object-Oriented version)
"""
from ascii_art import display_title
from game import TicTacToeGame
from ui_utils import print_info, print_success, colored_text, Colors

def main():
    """Main function to run the game."""
    # Display title
    display_title()
    
    # Main program loop
    play_again = True
    game = TicTacToeGame()
    
    while play_again:
        # Setup and play a new game
        game.setup_game()
        game.play()
        
        # Display statistics
        game.display_stats()
        
        # Ask if the player wants to play again
        print_info("\n------------------------")
        print_info("Want to challenge your skills again?")
        
        while True:
            choice = input(f"Do you want to play again? ({colored_text('yes', Colors.GREEN)}/{colored_text('no', Colors.RED)}): ").strip().lower()
            if choice == 'yes' or choice == 'y':
                print_success("Great! Let's play another round!")
                break
            elif choice == 'no' or choice == 'n':
                play_again = False
                print_success("\nThanks for playing! Goodbye! 👋")
                break
            else:
                print(f"{colored_text('Invalid input.', Colors.RED)} Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()