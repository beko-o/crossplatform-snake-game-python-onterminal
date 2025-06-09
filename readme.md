# 🐍 Terminal Snake Game

A classic Snake game implementation for the terminal/command line, built with Python. Play the nostalgic Snake game right in your terminal with smooth gameplay and cross-platform compatibility!

![Snake Game Demo](https://img.shields.io/badge/Game-Snake-green?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-yellow?style=for-the-badge&logo=python)

## 🎮 Game Features

- **Smooth Gameplay**: Optimized rendering with no screen flicker
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Dual Controls**: Arrow keys OR WASD movement
- **Score Tracking**: Earn points for each food consumed
- **Collision Detection**: Wall and self-collision detection
- **Growing Snake**: Snake grows longer as you eat food
- **Clean Interface**: Minimalist terminal-based UI

## 🎯 Game Rules

- Control the snake to eat food (`*`) and grow longer
- Avoid hitting the walls (`#`) or the snake's own body
- Each food gives you 10 points
- The game ends when you collide with walls or yourself
- Try to achieve the highest score possible!

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Terminal/Command Prompt

### Installation & Running

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/terminal-snake-game.git
   cd terminal-snake-game
   ```

2. **Run the game**
   ```bash
   python snake_game.py
   ```

3. **Start playing!**
   - Follow the on-screen instructions
   - Use arrow keys or WASD to control the snake
   - Press 'q' to quit anytime

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ Arrow / W | Move Up |
| ↓ Arrow / S | Move Down |
| ← Arrow / A | Move Left |
| → Arrow / D | Move Right |
| Q | Quit Game |

## 🎨 Game Elements

| Symbol | Description |
|--------|-------------|
| `O` | Snake Head |
| `o` | Snake Body |
| `*` | Food |
| `#` | Wall/Border |

## 🛠️ Technical Details

### Cross-Platform Compatibility

The game automatically detects your operating system and uses the appropriate input method:

- **Windows**: Uses `msvcrt` module for keyboard input
- **Unix/Linux/macOS**: Uses `termios` and `select` modules

### Performance Optimizations

- **Fast Screen Clearing**: Uses ANSI escape codes instead of system calls
- **Optimized Rendering**: Builds entire screen as single string for faster output
- **Smooth Animation**: Reduced input delay and optimized game loop

## 📁 Project Structure

```
terminal-snake-game/
│
├── snake_game.py          # Main game file
├── README.md             # This file
└── LICENSE               # License file
```

## 🔧 Dependencies

The game uses only Python standard library modules:

- `random` - For food placement
- `sys` - For system operations
- `os` - For cross-platform compatibility
- `time` - For game timing
- `msvcrt` (Windows) / `termios` (Unix) - For keyboard input

**No external packages required!**

## 🎯 Gameplay Tips

1. **Plan Your Route**: Think ahead to avoid trapping yourself
2. **Use the Walls**: Navigate close to borders for better control
3. **Stay Calm**: Don't panic when the snake gets longer
4. **Practice Makes Perfect**: Master the controls for higher scores

## 🐛 Troubleshooting

### Common Issues

**Game doesn't respond to arrow keys:**
- Try using WASD keys instead
- Ensure your terminal supports arrow key input

**Screen flickering:**
- The game uses optimized rendering to prevent this
- Try running in a different terminal if issues persist

**Import errors:**
- Ensure you're using Python 3.6+
- All required modules are part of Python's standard library

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Bug Reports**: Found a bug? Please open an issue
2. **Feature Requests**: Have ideas for new features? Let us know!
3. **Code Improvements**: Submit pull requests for enhancements
4. **Documentation**: Help improve the documentation

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly on different platforms
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Python's standard library for maximum compatibility
- Thanks to the Python community for excellent documentation

## 📈 Future Enhancements

- [ ] High score persistence
- [ ] Multiple difficulty levels
- [ ] Color support for terminals
- [ ] Sound effects (where supported)
- [ ] Multiplayer mode
- [ ] Custom game board sizes

---

**Enjoy the game! 🐍**

*Star ⭐ this repository if you found it helpful!*
