# ANSI color codes
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def colored_text(text, color):
    """Returns colored text using ANSI color codes"""
    return f"{color}{text}{Colors.RESET}"

def print_info(message):
    """Prints an information message in blue"""
    print(colored_text(message, Colors.BLUE))

def print_success(message):
    """Prints a success message in green"""
    print(colored_text(message, Colors.GREEN))

def print_warning(message):
    """Prints a warning message in yellow"""
    print(colored_text(message, Colors.YELLOW))

def print_error(message):
    """Prints an error message in red"""
    print(colored_text(message, Colors.RED))