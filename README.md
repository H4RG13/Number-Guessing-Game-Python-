# 🎲 Number Guessing Game

A fun, interactive number guessing game built with Flask and Python. The computer picks a number between 1-100, and you have unlimited attempts to guess it!

## Features

✨ **Core Features:**
- 🎯 Interactive number guessing with instant feedback
- 📊 Attempt counter to track your progress
- 💾 Session-based state management (uses Flask sessions)
- 🎨 Beautiful, responsive UI with modern styling
- ♿ Accessible HTML with proper semantic structure

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML5, CSS3
- **Session Management:** Flask sessions

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup

1. **Clone or navigate to the project:**
   ```bash
   cd "Number Guessing Game"
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   - Navigate to `http://localhost:5000`
   - Start playing!

## How to Play

1. The game thinks of a number between 1 and 100
2. Enter your guess in the input field
3. The game tells you if your guess is **too high** or **too low**
4. Keep guessing until you find the correct number
5. Your attempt count increases with each guess
6. When you guess correctly, you can start a new game!

## Code Structure

### `app.py`
Main Flask application with:
- **`index()` route:** Handles game logic and guess validation
- **`reset()` route:** Allows players to start a new game
- Input validation for edge cases (empty input, out of range, non-numeric)
- Better error handling with specific exception types

### `templates/index.html`
Beautiful responsive UI featuring:
- Modern gradient background
- Smooth animations and transitions
- Color-coded feedback messages
- Mobile-friendly design
- Professional styling

## Improvements Made

- ✅ Input validation (bounds checking, type checking)
- ✅ Attempt tracking for better UX
- ✅ Semantic HTML structure
- ✅ Professional CSS styling with animations
- ✅ Better error messages with visual feedback
- ✅ Dedicated reset button/route
- ✅ Improved code comments and documentation
- ✅ Better exception handling

## Future Enhancements

- Add difficulty levels (different ranges)
- Implement leaderboard/high scores
- Add sound effects and haptic feedback
- Store statistics (average attempts, best time)
- Implement streak counter
- Add dark mode toggle

## License

This is a practice project. Feel free to use and modify as needed!
