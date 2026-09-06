# Checkers Game with Minimax AI

<p align="center">
  <img src="visuals/banner.png" width="100%" alt="Checkers Game Banner">
</p>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Powered%20by-Pygame-green?style=for-the-badge)
<!-- BEGIN LATEST DOWNLOAD BUTTON -->

[![Download Checkers.exe](https://custom-icon-badges.demolab.com/badge/-Download%20Checkers.exe-blue?style=for-the-badge&logo=download&logoColor=white "Download Checkers.exe")](https://github.com/psycocodes/checkers-pygame/releases/download/v1.0/Checkers.exe)

<!-- END LATEST DOWNLOAD BUTTON -->


A classic checkers game built with Python and Pygame, featuring an intelligent AI opponent.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/psycocodes/checkers-pygame.git
   cd checkers-pygame
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Build a release for itch.io

The game is distributed as a desktop executable built with PyInstaller. Build
on each operating system you want to support; PyInstaller does not cross-build
Windows, Linux, and macOS executables.

1. Install the runtime and build dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-build.txt
   ```

2. Build the release archive:

   ```bash
   python build_release.py
   ```

   This creates `releases/Checkers-windows.zip` on Windows (or a corresponding
   Linux/macOS archive). The archive contains the executable and bundled game
   assets, so players do not need Python or Pygame installed.

3. In the itch.io project dashboard, create a downloadable file and upload the
   archive. Mark it for the matching platform and architecture, then set the
   launch file to `Checkers.exe` on Windows or `Checkers` on Linux/macOS.

For Windows, build from a Windows machine and upload the resulting
`Checkers-windows.zip`. Test the extracted executable before publishing.

## Features

- Interactive gameplay with classic checkers rules
- AI opponent with multiple difficulty levels
- Custom graphics and animations
- Particle effects and visual feedback
- Sound effects and background music

## Screenshots

<table width="100%" style="border: none;">
  <tr>
    <td width="50%" style="border: none;"><img src="screenshots/01.png" width="100%" alt="Main Menu"/></td>
    <td width="50%" style="border: none;"><img src="screenshots/02.png" width="100%" alt="Gameplay"/></td>
  </tr>
  <tr>
    <td width="50%" style="border: none;"><img src="screenshots/03.png" width="100%" alt="Mid-Game"/></td>
    <td width="50%" style="border: none;"><img src="screenshots/04.png" width="100%" alt="Victory Screen"/></td>
  </tr>
</table>

## AI Algorithm - Minimax

The game implements the Minimax algorithm with alpha-beta pruning for the AI opponent. This algorithm evaluates all possible future game states to make optimal moves.

<p align="center">
  <img src="visuals/checkers.png" width="100%" alt="Checkers Game">
</p>

### How it works:

- **Minimax Tree**: Explores all possible moves up to a certain depth
- **Alpha-Beta Pruning**: Eliminates branches that won't affect the final decision
- **Evaluation Function**: Scores board positions based on piece count, position, and king status
- **Difficulty Levels**:
  - Easy (Depth 2): Quick decisions, good for beginners
  - Medium (Depth 4): Balanced gameplay with moderate challenge
  - Hard (Depth 6): Deep analysis, challenging for experienced players

## Game Rules

- Players alternate turns moving pieces diagonally
- Capture opponent pieces by jumping over them
- Pieces become kings when reaching the opposite end
- Kings can move both forward and backward
- Win by capturing all opponent pieces or blocking their moves

## Project Structure

```
checkers-pygame/
├── Assets/              # Game assets (images, sounds, fonts)
├── Checkers/            # Core game logic
│   ├── algorithm.py     # AI minimax implementation
│   ├── board.py         # Game board logic
│   ├── game.py          # Main game controller
│   └── piece.py         # Piece object and logic
├── GUI/                 # User interface components
├── main.py              # Game entry point
├── screen_manager.py    # Screen state management
└── requirements.txt     # Dependencies
```

## Technical Details

- **Language**: Python 3.7+
- **Game Engine**: Pygame 2.6.1
- **Architecture**: Modular design with separated concerns
- **Cross-Platform**: Windows, macOS, Linux support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: [psycocodes](https://github.com/psycocodes)
- **Repository**: [checkers-pygame](https://github.com/psycocodes/checkers-pygame)
