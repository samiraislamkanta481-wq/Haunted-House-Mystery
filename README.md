# Haunted House Mystery

**Name:** Samira Islam Kanta
**Student ID:** 11230321317

## About the Game

Haunted House Mystery is a horror-themed hidden object adventure game developed using Python (pygame). The player explores multiple haunted rooms with only a flashlight, discovers hidden objects, solves puzzles, and uncovers the mystery to escape the haunted house before time runs out.

## How to Play

* Click the **Start Game** button to begin.
* Use the mouse (flashlight) to explore the dark room and find hidden objects.
* Click on hidden objects to collect them.
* Solve puzzles to discover clues and unlock further rooms.
* Keep an eye on the countdown timer.
* Avoid incorrect clicks to prevent time penalties.
* Complete the challenges to progress through the game.

## Features

* Horror-themed haunted house environment (dark rooms, flashlight effect, lightning, floating spirits).
* Multiple haunted rooms (4 rooms).
* Hidden-object searching.
* Individual object images with transparent backgrounds.
* Puzzle-solving challenges.
* Countdown timer for each room.
* Score tracking system (best score is saved).
* Incorrect-click detection.
* Time penalty system.
* Inventory system.
* Room progression.
* Game-over screen.
* Restart option.

## Rooms

| Room | Hidden Objects | Puzzle |
|------|----------------|--------|
| 1. The Silent Foyer | Key, Candle, Skull, Doll, Locket, Lantern | Code lock |
| 2. Whispering Library | Book, Ring, Hourglass, Raven, Scissors, Eye | Candle sequence memory |
| 3. The Cursed Bedroom | Mask, Cross, Bell, Potion, Dagger, Key | Mirror riddle |
| 4. The Blood Cellar | Skull, Candle, Dagger, Potion, Eye, Bell | Relic order puzzle |

## Scoring and Penalties

* Each object found: **+100 points**
* Each puzzle solved: **+250 points**
* Time bonus: **+5 points per second left** when a room is cleared
* Wrong click: **-5 seconds** and **-25 points**
* Hint: **-10 seconds** (2 hints per room)

## Controls

| Key / Action | Function |
|--------------|----------|
| Mouse move | Move the flashlight |
| Left click | Collect an object / press puzzle buttons |
| H | Use a hint |
| P or Esc | Pause the game |
| Enter | Submit the code in the code-lock puzzle |
| R | Restart (game-over / victory screen) |
| M | Return to main menu (pause / game-over / victory screen) |

## Project Structure

Game2/
├── haunted_house_mystery.py   # main game file
├── README.md
├── best_score.txt             # created automatically after the first game
└── assets/
    └── objects/               # optional custom PNG images

    <img width="1277" height="852" alt="Screenshot 2026-11-26 155953" src="https://github.com/user-attachments/assets/300f92dc-2a46-4636-9110-1836f266d944" />

