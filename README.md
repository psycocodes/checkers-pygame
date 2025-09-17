# 🏁 Checkers Game with AI

A fully-featured checkers game built with Python and Pygame, featuring stunning graphics, particle effects, AI opponent, and immersive sound effects.

## ✨ Features

- 🎮 **Interactive Gameplay** - Classic checkers rules with smooth piece movement
- 🤖 **AI Opponent** - Intelligent AI with multiple difficulty levels (Easy, Medium, Hard)
- 🎨 **Beautiful Graphics** - Custom pixel art pieces and animated backgrounds
- ✨ **Particle Effects** - Dynamic particle system for enhanced visual experience
- 🔊 **Sound Effects** - Immersive audio feedback for moves, captures, and victories
- 🎵 **Background Music** - Atmospheric soundtrack to enhance gameplay
- 👑 **King Pieces** - Automatic promotion when pieces reach the opposite end
- 🏆 **Win Detection** - Automatic game end detection with victory screen

## 🎯 Game Rules

- Players alternate turns moving their pieces diagonally
- Capture opponent pieces by jumping over them
- Pieces become "kings" when they reach the opposite end of the board
- Kings can move both forward and backward
- Win by capturing all opponent pieces or blocking all their moves

## 🎮 Controls

- **Mouse Click** - Select and move pieces
- **ESC** - Exit game or return to menu
- **Difficulty Selection** - Choose AI difficulty before starting

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/psycocodes/checkers-pygame.git
   cd checkers-pygame
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🖼️ Screenshots

### Main Menu

![Main Menu](screenshots/01.png)
_Sleek main menu with difficulty selection and dynamic particle effects_

### Gameplay - Piece Selection

![Gameplay Selection](screenshots/02.png)
_Interactive gameplay showing piece selection and highlighted valid moves_

### Mid-Game Action

![Mid-Game](screenshots/03.png)
_Intense checkers action with AI opponent making strategic moves_

### Victory Screen

![Victory Screen](screenshots/04.png)
_Victory celebration screen with options to play again or quit_

## 🏗️ Project Structure

```
checkers-pygame/
├── Assets/                     # Game assets
│   ├── *.png                  # Images and sprites
│   ├── *.wav                  # Sound effects
│   ├── *.mp3                  # Background music
│   ├── *.ttf                  # Custom fonts
│   └── *.json                 # Configuration files
├── Checkers/                  # Core game logic
│   ├── algorithm.py           # AI minimax algorithm
│   ├── board.py              # Game board logic
│   ├── constants.py          # Game constants
│   ├── game.py               # Main game controller
│   └── piece.py              # Piece object and logic
├── GUI/                       # User interface components
│   ├── button.py             # Interactive buttons
│   ├── constants.py          # UI constants
│   ├── gui.py                # Main menu interface
│   ├── infinite_bg.py        # Animated background
│   ├── particle_system.py    # Particle effects
│   ├── sound_manager.py      # Audio management
│   ├── textures.py           # Asset loading
│   └── vfx.py                # Visual effects
├── main.py                    # Game entry point
├── screen_manager.py          # Screen state management
├── asset_utils.py             # Asset path utilities
└── requirements.txt           # Python dependencies
```

## 🧠 AI Algorithm

The game features a sophisticated AI opponent using the **Minimax algorithm** with the following characteristics:

- **Minimax with Alpha-Beta Pruning** - Efficient game tree search
- **Multiple Difficulty Levels**:
  - 🟢 **Easy** (Depth 2) - Good for beginners
  - 🟡 **Medium** (Depth 4) - Balanced challenge
  - 🔴 **Hard** (Depth 6) - Expert level AI
- **Position Evaluation** - Considers piece value, position, and king status
- **Strategic Planning** - Looks ahead multiple moves to make optimal decisions

## 🎨 Graphics & Effects

- **Custom Pixel Art** - Hand-crafted piece sprites and UI elements
- **Particle System** - Dynamic background effects and animations
- **Smooth Animations** - Fluid piece movement and transitions
- **Retro Aesthetic** - Classic arcade-style fonts and color schemes

## 🔊 Audio

- **Immersive Sound Design** - Distinct sounds for different game events
- **Background Music** - Atmospheric tracks to enhance gameplay
- **Audio Feedback** - Click sounds, move sounds, capture effects, and victory music

## 🛠️ Technical Details

- **Engine**: Pygame 2.6.1
- **Language**: Python 3.7+
- **Architecture**: Modular design with separated concerns
- **Performance**: Optimized rendering and efficient game loop
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- 🎮 New game modes (multiplayer, tournaments)
- 🎨 Additional themes and graphics
- 🤖 Enhanced AI algorithms
- 🔊 More sound effects and music
- 🌐 Localization and translations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pygame Community** - For the excellent game development framework
- **Contributors** - Thanks to all who have contributed to this project
- **Testers** - Everyone who helped test and improve the game

## 📞 Contact

- **Author**: [psycocodes](https://github.com/psycocodes)
- **Repository**: [checkers-pygame](https://github.com/psycocodes/checkers-pygame)
- **Issues**: [Report bugs or request features](https://github.com/psycocodes/checkers-pygame/issues)

---

### 🎮 Ready to Play?

```bash
git clone https://github.com/psycocodes/checkers-pygame.git
cd checkers-pygame
pip install pygame
python main.py
```

**Enjoy the game and may the best strategist win!** 🏆
