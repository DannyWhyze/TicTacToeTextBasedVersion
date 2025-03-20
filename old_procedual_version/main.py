import sys
import os

# Füge übergeordnetes Verzeichnis zum Pfad hinzu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ascii_art import display_title
from old_procedual_version.startGame import play_game
from ui_utils import print_info, print_success, colored_text, Colors

# Display title
display_title()

# Main program loop
play_again = True
while play_again:
    play_game()
    
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

