"""
50 Python Games - Main Launcher
Run this file to choose and play any of the 50 games.
"""
import importlib.util
import os
import sys

# Directory where this script and game_*.py files live
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# List of (module_name, display_name, entry_function_name)
GAMES = [
    ("game_01_fortune_cookie", "Fortune Cookie", "fortune_cookie"),
    ("game_02_dice_roller", "Dice Rolling Simulator", "dice_roller"),
    ("game_03_rock_paper_scissors", "Rock Paper Scissors", "rock_paper_scissors"),
    ("game_04_rock_paper_scissors_lizard_spock", "Rock Paper Scissors Lizard Spock", "rock_paper_scissors_lizard_spock"),
    ("game_05_millionaire", "Who Wants to Be a Millionaire", "millionaire_game"),
    ("game_06_quiz_game", "Quiz Game", "quiz_game"),
    ("game_07_text_adventure", "Text-Based Adventure", "text_adventure"),
    ("game_08_chatbot", "Chatbot", "chatbot"),
    ("game_09_truth_or_dare", "Truth or Dare", "truth_or_dare"),
    ("game_10_leap_year_checker", "Leap Year Checker", "leap_year_checker"),
    ("game_11_baby_blackjack", "Baby Blackjack", "baby_blackjack"),
    ("game_12_blackjack", "Blackjack", "blackjack"),
    ("game_13_metric_converter", "Metric Conversion Tool", "metric_converter"),
    ("game_14_area_calculator", "Area Calculator", "area_calculator"),
    ("game_15_guess_number", "Guess My Number", "guess_number"),
    ("game_16_word_counter", "Word Counter", "word_counter"),
    ("game_17_morse_translator", "Morse Code Translator", "morse_translator"),
    ("game_18_roman_converter", "Roman Numeral Converter", "roman_converter"),
    ("game_19_metrocard_calculator", "NYC MetroCard Calculator", "metrocard_calculator"),
    ("game_20_caesar_cipher", "Caesar Cipher", "caesar_cipher"),
    ("game_21_bank_account", "Bank Account System", "bank_system"),
    ("game_22_horoscope", "Horoscope", "horoscope"),
    ("game_23_todo_list", "To-Do List Manager", "todo_app"),
    ("game_24_grocery_list", "Grocery List Manager", "grocery_app"),
    ("game_25_favorites_manager", "Favorites Manager", "favorites_manager"),
    ("game_26_class_schedule", "Class Schedule Manager", "class_schedule"),
    ("game_27_expense_tracker", "Expense Tracker", "expense_tracker_app"),
    ("game_28_library", "Library Management System", "library_app"),
    ("game_29_contact_book", "Contact Book", "contact_app"),
    ("game_30_recipe_book", "Recipe Book", "recipe_app"),
    ("game_31_pokedex", "Pokédex", "pokedex"),
    ("game_32_hangman", "Hangman", "hangman"),
    ("game_33_tic_tac_toe", "Tic-Tac-Toe", "tic_tac_toe"),
    ("game_34_battleship", "Battleship", "battleship"),
    ("game_35_connect_four", "Connect Four", "connect_four"),
    ("game_36_snake_game", "Snake Game", "snake_game"),
    ("game_37_pong_game", "Pong Game", "pong_game"),
    ("game_38_space_invaders", "Space Invaders", "space_invaders"),
    ("game_39_game_2048", "2048 Game", "game_2048"),
    ("game_40_wordle_game", "Wordle Game", "wordle_game"),
    ("game_41_alarm_clock", "Alarm Clock", "alarm_clock"),
    ("game_42_gui_calculator", "GUI Calculator", "gui_calculator"),
    ("game_43_tetris_game", "Tetris Game", "tetris_game"),
    ("game_44_cards_against_humanity", "Cards Against Humanity", "cards_against_humanity"),
    ("game_45_trex_run", "T-Rex Run", "trex_run"),
    ("game_46_minesweeper", "Minesweeper", "minesweeper"),
    ("game_47_paint_program", "Paint Program", "paint_program"),
    ("game_48_battleship_enhanced", "Enhanced Battleship", "battleship_enhanced"),
    ("game_49_yahtzee", "Yahtzee", "yahtzee_game"),
    ("game_50_darts_game", "Darts Game", "darts_game"),
]


def run_game(module_name: str, entry_func: str) -> None:
    """Load and run a game module by name."""
    path = os.path.join(SCRIPT_DIR, f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        print(f"Could not load {module_name}.py")
        return
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"Error loading game: {e}")
        return
    func = getattr(mod, entry_func, None)
    if func is None:
        print(f"Game has no function '{entry_func}'")
        return
    func()


def main():
    # Fix Windows console encoding for emojis
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    print("🎯 50 Python Games - Launcher 🎯")
    print("=" * 50)
    print("\nChoose a game to run (or '0' to exit):\n")

    for i in range(0, 50, 2):
        key1 = str(i + 1).rjust(2)
        name1 = GAMES[i][1]
        key2 = str(i + 2).rjust(2) if i + 2 <= 50 else ""
        name2 = GAMES[i + 1][1] if i + 2 <= 50 else ""
        print(f"  {key1}. {name1:32}  {key2}. {name2}")

    while True:
        choice = input("\nEnter game number (1-50): ").strip()

        if choice == "0":
            print("Goodbye! 👋")
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 50:
            print("Invalid choice. Enter a number 1-50 or 0 to exit.")
            continue

        idx = int(choice) - 1
        module_name, display_name, entry_func = GAMES[idx]

        print(f"\n{'=' * 60}")
        print(f"  Running: {display_name}")
        print("=" * 60)
        try:
            run_game(module_name, entry_func)
        except KeyboardInterrupt:
            print("\n\nReturning to menu...")
        except ImportError as e:
            print(f"\nMissing dependency: {e}")
            print("Some games need: pip install windows-curses  (Snake on Windows)")
            print("                pip install pygame           (Pong, Space Invaders, etc.)")
            print("                pip install tkinter          (often included with Python)")
        except Exception as e:
            print(f"\nError: {e}")
        print(f"\n{'=' * 60}")
        print("Back to menu.")
        print("=" * 60)


if __name__ == "__main__":
    main()
