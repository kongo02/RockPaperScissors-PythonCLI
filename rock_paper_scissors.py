import random
import time


def get_computer_choice(game):
    """Select a random choice for the computer."""
    return random.choice(list(game.keys()))


def print_choices(user_choice, computer_choice, game):
    """Print both the user and computer choices."""
    time.sleep(1)
    print()
    print("\t👧 PLAYER:", game[user_choice].upper())
    print()
    time.sleep(1)
    print("\t💻 COMPUTER:", game[computer_choice].upper())
    print()


def determine_winner(user_choice, computer_choice):
    """Return the result of the game."""
    winnig_combinations = {1: 2, 2: 3, 3: 1}
    if user_choice == computer_choice:
        return "TIE GAME 🔄"
    elif winnig_combinations[user_choice] == computer_choice:
        return "PLAYER WIN 🏆"
    else:
        return "COMPUTER WIN 🏆"


def main():
    print()
    game = {1: "rock", 2: "scissors", 3: "paper"}
    print("+++++++++++++++ 🎯 WELCOME TO THE GAME 🎯 +++++++++++++++++++++")
    print()
    print("+++++++++++++++ 🕹 CHOOSE OPTION BELOW 🕹 +++++++++++++++++++++++")
    print()
    print("1 FOR ROCK 💎 | 2 FOR SCISSORS ✂ | 3 FOR PAPER 🧻 | OR 'Q' TO QUIT ❌")
    print("========================================================================")
    print()

    while True:
        print()
        user_input = input("ENTER YOUR CHOICE ⏯ : ").strip().lower()

        if user_input == "q":
            print()
            print("GOOD BYE 👋🏻.")
            print()
            break

        try:
            user_choice = int(user_input)
            if user_choice not in game.keys():
                print()
                print("INVALID OPTION ⛔")
                print()
                continue

        except ValueError:
            print()
            print("ENTER ONLY 1 | 2 | 3 OR 'Q' TO QUIT ")
            print()
            continue

        computer_choice = get_computer_choice(game)
        print_choices(user_choice, computer_choice, game)
        result = determine_winner(user_choice, computer_choice)
        print(f"\t{result}")
        print()

        # Ask if the user wants to play again
        if input(
            "DO YOU WANT TO PLAY AGAIN ⏯ ('Y' OR ANY KEYS TO QUIT): "
        ).strip().lower() not in ["y", "yes"]:
            print()
            print("THANKS FOR PLAYING 🙏!")
            print()
            break


# Unit tests
def test_determine_winner():
    assert determine_winner(1, 2) == "PLAYER WIN 🏆"  # Rock beats Scissors
    assert determine_winner(2, 3) == "PLAYER WIN 🏆"  # Scissors beats Paper
    assert determine_winner(3, 1) == "PLAYER WIN 🏆"  # Paper beats Rock
    assert determine_winner(1, 1) == "TIE GAME 🔄"  # Rock vs Rock
    assert determine_winner(2, 2) == "TIE GAME 🔄"  # Scissors vs Scissors
    assert determine_winner(3, 3) == "TIE GAME 🔄"  # Paper vs Paper
    assert determine_winner(2, 1) == "COMPUTER WIN 🏆"  # Scissors loses to Rock
    assert determine_winner(3, 2) == "COMPUTER WIN 🏆"  # Paper loses to Scissors
    assert determine_winner(1, 3) == "COMPUTER WIN 🏆"  # Rock loses to Paper


if __name__ == "__main__":
    main()
