# Dots and Boxes Game

## Overview
Dots and Boxes is a classic strategic turn-based game implemented in Python using the Pygame library. Players take turns connecting dots on a grid, and when a player completes a box, they claim it and take another turn. The player with the most boxes at the end of the game wins.

## Features
- Three different grid sizes: 5x5, 6x6, and 7x7
- Two-player gameplay
- Visual feedback with color-coded elements:
  - Red for Player 1
  - Blue for Player 2
- Sound effects for line creation and box completion
- Score tracking
- Clean and intuitive user interface

## Requirements
- Python 3.x
- Pygame library

## Installation
1. Make sure you have Python installed on your system
2. Install Pygame using pip:
   ```
   pip install pygame
   ```
3. Download the game files to your local directory
4. Ensure you have sound files (1.wav) in the same directory as the main.py file

## How to Play
1. Run the game:
   ```
   python main.py
   ```
2. In the main menu, select a grid size (5x5, 6x6, or 7x7)
3. Players take turns clicking on the spaces between dots to draw lines
4. When a player completes a box, it's filled with their color and they get an extra turn
5. The game ends when all boxes are filled
6. The player with the most boxes wins

## Controls
- **Mouse**: Click between dots to place lines
- Close the window to exit the game

## Game Rules
1. Players alternate turns drawing a single line between two adjacent dots
2. When a player completes the fourth side of a box, they claim it and get another turn
3. The game ends when all possible lines have been drawn and all boxes are claimed
4. The player with the most boxes wins

## File Structure
- `main.py` - The main game code
- `1.wav` - Sound effect file for game actions

## Credits
This implementation of Dots and Boxes was created using Python and the Pygame library.