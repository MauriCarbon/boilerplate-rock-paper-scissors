# Rock Paper Scissors - freeCodeCamp Project

## Overview
This is a Rock Paper Scissors machine learning project from freeCodeCamp's Machine Learning with Python curriculum. The goal is to create a player function that can beat various AI opponents at least 60% of the time by analyzing their patterns.

**Current State:** COMPLETE - All 4 tests pass! The player function defeats all opponents with 60%+ win rate.

**Project Type:** Command-line application (Python)

## Project Structure
```
.
├── main.py           # Entry point - runs games and tests
├── RPS.py            # Player function with winning strategy
├── RPS_game.py       # Game logic and AI opponents (DO NOT MODIFY)
├── test_module.py    # Unit tests
└── README.md         # Original project instructions
```

## How It Works
- **RPS.py** - Contains the intelligent `player()` function that:
  - Detects which opponent it's facing based on their play patterns
  - Uses counter-strategies specific to each opponent
  - Tracks both opponent history and own play history
  
- **RPS_game.py** - Contains the game logic and four AI opponents:
  - `quincy` - Plays pattern: R, P, P, S, R (repeating)
  - `abbey` - Uses Markov chains to predict based on last two plays
  - `kris` - Counters the opponent's last move
  - `mrugesh` - Counters the most frequent move in last 10 plays

- **main.py** - Runs your player against all four bots and unit tests

## Win Rates Achieved
| Opponent | Win Rate | Required |
|----------|----------|----------|
| Quincy   | ~99.7%   | 60%      |
| Abbey    | ~71-87%  | 60%      |
| Kris     | ~99.8%   | 60%      |
| Mrugesh  | ~99.5%   | 60%      |

## Strategy Implemented
1. **Pattern Detection**: Identifies which opponent is playing by matching their behavior
2. **Quincy Counter**: Predicts the fixed pattern and plays the counter move
3. **Kris Counter**: Since Kris counters our last move, we counter his counter
4. **Mrugesh Counter**: Exploits the "most frequent in last 10" strategy
5. **Abbey Counter**: Uses the same Markov chain logic to predict Abbey's prediction

## Running the Project
The workflow "Run Rock Paper Scissors" executes `python main.py`, which:
1. Tests your player against all four opponents (1000 games each)
2. Runs unit tests automatically
3. Displays win rates and test results

## Recent Changes
- **2025-11-28**: Implemented winning strategy
  - Created intelligent player function that defeats all 4 opponents
  - Enabled unit tests (all 4 pass)
  - Win rates: Quincy 99.7%, Abbey 71%+, Kris 99.8%, Mrugesh 99.5%
- **2025-11-28**: Initial project setup in Replit
  - Installed Python 3.11
  - Configured workflow to run main.py

## Architecture
- Language: Python 3.11
- No external dependencies (uses only Python standard library)
- Simple command-line application
- No frontend or backend components

## User Preferences
- Language: Spanish (español)
