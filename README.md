# ♟ Floomze Chess

**Floomze Chess** is a custom Python chess application developed from the ground up. The project uses **Tkinter**, **Python-Chess**, and **Pygame** to provide a graphical chess experience with custom pieces, sounds, game-state detection, pawn promotion, and modular code.

> Created by **DrFrostij**

---

## Features

### ♟ Chess System
- Full 8×8 chessboard
- Legal chess movement
- Turn-based gameplay
- Piece selection using mouse input
- Captures
- Castling
- Pawn promotion
- Queen promotion
- Rook promotion
- Bishop promotion
- Knight promotion
- Checkmate detection
- Stalemate detection
- Insufficient-material detection
- Automatic winner detection

### 🎨 Graphical Interface
- Custom Tkinter interface
- Custom chessboard design
- Custom chess piece images
- Custom application icon
- 1000×1000 main window
- Custom menus
- Credits menu
- Exit menu

### 🔊 Sound System
Floomze Chess includes custom sound effects for different game events:

- Game start
- Normal moves
- Captures
- Castling
- Pawn promotion
- Illegal moves
- Game end

### 🧩 Modular Architecture

The project is separated into multiple Python files so different parts of the application can be developed independently.

```text
Floomze Chess/
│
├── FloomzeChess.py
├── chessboardmoves.py
├── piecesimages.py
│
├── icons/
│   └── chessicon.png
│
└── sounds/
    ├── game-start.mp3
    ├── move-self.mp3
    ├── capture.mp3
    ├── castle.mp3
    ├── promote.mp3
    ├── illegal.mp3
    └── game-end.mp3
```

---

## Technologies

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Tkinter** | Graphical user interface |
| **Python-Chess** | Chess rules and legal move generation |
| **Pygame** | Audio and sound effects |
| **CustomTkinter** | Additional GUI development |
| **Hashlib** | Data hashing for future systems |

---

## Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check your installation:

```cmd
python --version
```

or:

```cmd
py --version
```

### 2. Install Python-Chess

```cmd
py -m pip install python-chess
```

### 3. Install Pygame

```cmd
py -m pip install pygame-ce
```

### 4. Install CustomTkinter

```cmd
py -m pip install customtkinter
```

---

## Running Floomze Chess

Clone the repository:

```cmd
git clone <repository-url>
```

Enter the project directory:

```cmd
cd Floomze-Chess
```

Run the application:

```cmd
py FloomzeChess.py
```

---

## How It Works

Floomze Chess uses **Python-Chess** to handle the underlying chess rules rather than manually implementing every chess rule.

The application creates a `chess.Board()` object which maintains the current position and turn.

When a player clicks a square, the program converts the mouse coordinates into a chess square:

```python
square = square_from_mouse(event)
```

A `chess.Move` is then created and checked against the board's legal moves:

```python
if move in board.legal_moves:
    board.push(move)
```

This prevents illegal chess moves from being played.

After every successful move, the graphical board is redrawn to reflect the updated position.

---

## Pawn Promotion

When a pawn reaches the opposite side of the board, Floomze Chess opens a promotion window.

The player can select:

- Queen
- Rook
- Bishop
- Knight

The selected piece is then passed to Python-Chess as part of the move.

---

## Game States

The application checks for several terminal game states:

```python
board.is_checkmate()
board.is_stalemate()
board.is_insufficient_material()
```

When checkmate occurs, the application determines the winning side and displays a checkmate message.

---

## Sound System

Sounds are stored inside the `sounds` directory.

The application loads sounds dynamically based on the event:

```python
play_sound("capture.mp3")
```

This allows individual game events to have their own audio feedback.

---

## Development

Floomze Chess is an ongoing development project.

Planned development includes:

- Human vs AI
- Human vs Human game modes
- AI difficulty selection
- Elo-based AI difficulty
- Improved graphical interface
- Move highlighting
- Check highlighting
- Better menus
- Game statistics
- Additional chess features
- Improved error handling
- Further code optimisation

---

## Project Goals

The project is designed to demonstrate practical Python development through a larger multi-file application.

Key development areas include:

- Object-oriented and modular programming
- GUI development
- Event-driven programming
- External Python libraries
- File handling
- Audio handling
- Algorithmic chess logic
- User input processing
- Debugging
- Software development and testing

---

## Current Status

**Development Stage:** Early Development

The core chess functionality is operational, including board rendering, legal movement, captures, castling, promotion, game-state detection, custom graphics, and sound effects.

The project is being actively expanded toward a more complete chess application.

---

## Credits

**Developer:** DrFrostij

**Project:** Floomze Chess

Built with Python, Tkinter, Python-Chess, and Pygame.

---

## License

This project is currently a personal development project.

Unless otherwise stated, the source code and original assets should not be redistributed or used commercially without permission from the developer.
