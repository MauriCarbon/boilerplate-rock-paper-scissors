# Rock Paper Scissors - freeCodeCamp Project

## Overview
This is a Rock Paper Scissors machine learning project from freeCodeCamp's Machine Learning with Python curriculum. The goal is to create a player function that can beat various AI opponents at least 60% of the time by analyzing their patterns.

**Current State:** The project is fully set up and running in Replit. The basic example player function is implemented but has a low win rate (0-20% against different bots). Users need to improve the `player()` function in `RPS.py` to pass the challenge.

**Project Type:** Command-line application (Python)

## Project Structure
```
.
├── main.py           # Entry point - runs games and tests
├── RPS.py            # User's player function (to be modified)
├── RPS_game.py       # Game logic and AI opponents (DO NOT MODIFY)
├── test_module.py    # Unit tests
└── README.md         # Original project instructions
```

## How It Works
- **RPS.py** - Contains the `player()` function that you need to improve
- **RPS_game.py** - Contains the game logic and four AI opponents:
  - `quincy` - Plays a fixed pattern
  - `abbey` - Uses Markov chains to predict plays
  - `kris` - Counters the opponent's last move
  - `mrugesh` - Counters the most frequent move in last 10 plays
- **main.py** - Runs your player against all four bots

## Challenge Requirements
Your `player()` function must:
- Win at least 60% of games against each of the four AI opponents
- Track opponent history to detect patterns
- Return "R" (Rock), "P" (Paper), or "S" (Scissors)

## Running the Project
The workflow "Run Rock Paper Scissors" is configured to execute `python main.py`, which:
1. Tests your player against all four opponents (1000 games each)
2. Displays win rates for each matchup

## Testing
Uncomment line 20 in `main.py` to run the unit tests:
```python
main(module='test_module', exit=False)
```

## Recent Changes
- **2025-11-28**: Initial project setup in Replit
  - Installed Python 3.11
  - Configured workflow to run main.py
  - Project runs successfully with example player function

## Architecture
- Language: Python 3.11
- No external dependencies (uses only Python standard library)
- Simple command-line application
- No frontend or backend components

## User Preferences
None recorded yet.
