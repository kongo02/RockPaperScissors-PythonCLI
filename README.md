# RockPaperScissors-PythonCLI

## 🎯 Project Overview

This is a fun command-line game where players can challenge the computer in a classic game of Rock, Paper, Scissors! This project is built using Python and showcases basic CLI interactions, random choice generation, and game logic with built-in unit tests.

## 📋 Features
- User-friendly interface with emoji-enhanced displays.
- Game logic for Rock, Paper, Scissors with randomized computer choices.
- Play again option to allow multiple rounds.
- Clear, colorful display of choices and results.
- Built-in unit tests to validate the game rules.

## 🛠️ Installation and Setup
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/RockPaperScissors-PythonCLI.git
    cd RockPaperScissors-PythonCLI
    ```

2. **Run the Game**:
   - Make sure you have Python installed (version 3.6 or later).
   - Run the game from the command line:
     ```bash
     python game.py
     ```

## 🚀 Usage

1. Upon running the game, you'll be prompted to choose:
   - `1` for Rock 💎
   - `2` for Scissors ✂
   - `3` for Paper 🧻
   - `Q` to Quit ❌

2. After each round, the result will be displayed, showing whether the Player or Computer won or if it was a tie.

3. You can choose to play again or exit after each round.

## 🧪 Running Tests

The game includes basic unit tests for validating game logic. To run tests, execute:
```bash
python -m unittest game.py
