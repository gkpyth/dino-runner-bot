# Dino Runner Bot

A Python bot that automatically plays Chrome's offline dinosaur game by detecting obstacles in real time using screen capture and pixel brightness analysis. - part of bootcamp personal projects portfolio.

## Features
- Real-time screen capture around the cursor position
- Obstacle detection via pixel brightness analysis
- Supports both light mode and dark mode browser themes
- Automatic jump trigger using keyboard simulation
- Minimal setup — no game modification or browser extension required

## Requirements
- Python 3
- pyautogui
- mss
- numpy

## Installation
```
pip install -r requirements.txt
```

## How to Run
1. Open Chrome's dinosaur game (`https://elgoog.im/dinosaur-game/`) and start the game
2. Hover your cursor just ahead of the dinosaur on screen
3. Run the script:
```
python dino_bot.py
```
The bot will wait 3 seconds before starting, then monitor the screen region around your cursor and jump automatically when an obstacle is detected.

## How It Works
The bot captures a small region of pixels around your cursor position (determined by `constant`) on every loop iteration. It determines the background theme (light or dark) by averaging pixel brightness across the captured region. When a contrasting pixel cluster is detected — indicating an incoming obstacle — it simulates a spacebar press to jump.

| Theme | Obstacle Signal |
|-------|----------------|
| Light mode | Dark pixels detected in a light region |
| Dark mode | Light pixels detected in a dark region |

## Project Structure
```
dino-bot/
├── dino.py          # Main script — screen capture, detection, jump logic
└── requirements.txt
```

## Limitations
- Cursor must be manually positioned ahead of the dinosaur before running
- ~Recommended distance based on testing: roughly one dinosaur's width
- Detection is brightness-based and may misfire on cluttered or non-standard backgrounds
- No speed scaling — jump timing is reactive, not predictive
- Flying pterodactyls may not be detected reliably depending on cursor height
- ~Recommended height based on testing: upper limit of dinosaur's mouth 

## Author
Ghaleb Khadra