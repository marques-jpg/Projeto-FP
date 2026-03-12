# Orbito Board Game (Python Implementation)

## Overview
This repository contains a complete Python implementation of the abstract strategy board game **Orbito**. The project was developed as part of the "Fundamentos da Programação" (Programming Fundamentals) course. It features a fully functioning game engine that supports dynamic board sizes, the game's signature mechanical board rotations, and a built-in AI for single-player modes.

## Key Features & Mechanics
* **Dynamic Board Sizes (Orbito-n):** The game supports variable board dimensions ranging from 2 to 5 orbits, resulting in grid sizes from 4x4 up to 10x10.
* **Orbital Rotation:** Staying true to the physical game, the board "shifts" after every move. All stones automatically rotate one position counter-clockwise along their respective concentric orbits.
* **Win Condition:** A player wins by aligning a specific number of their stones (equal to the width of the board, e.g., 4 stones for Orbito-2) horizontally, vertically, or diagonally.
* **Strict Abstract Data Types (ADTs):** The codebase is thoroughly modular, using strictly defined ADTs for `Position`, `Stone`, and `Board`, ensuring robust state management and code readability.

## Game Modes
The main loop supports three different play modes:
1. **`2jogadores` (2 Players):** Local hot-seat multiplayer.
2. **`facil` (Easy AI):** Single-player mode against a basic computer opponent that makes standard automatic moves.
3. **`normal` (Normal AI):** Single-player mode against an improved computer opponent that actively tries to form lines and block the player's potential winning moves.

## How to Play
To start the game, load the script in your Python environment and call the main `orbito(n, lvl, pedra)` function. 

### Arguments:
* `n` (int): Number of orbits (from 2 to 5).
* `lvl` (str): The game mode (`'facil'`, `'normal'`, or `'2jogadores'`).
* `pedra` (str): The external representation of your stones (`'X'` for Black or `'O'` for White). Black always plays first.

### Example Usage:
```python
# Starts a 4x4 (2 orbits) game against the Easy AI, playing as Black ('X')
orbito(2, 'facil', 'X')

# Starts a local 2-player game on an 8x8 board (4 orbits)
orbito(4, '2jogadores', 'X')

## License

MIT License © 2025 Guilherme Marques.
