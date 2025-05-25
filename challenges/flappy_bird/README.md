# 🐦 Flappy Bird

A simple Flappy Bird clone built with python + pygame. This project is a recreation of the classic arcade-style game originally developed by .Gears. It's a great learning tool for game development and game physics fundamentals.

## 🎮 Game Overview

Flappy Bird is a side-scrolling arcade game where the player controls a bird, attempting to fly between sets of pipes without hitting them. The game ends when the bird collides with a pipe or the ground.

## 🧱 Core Components

### 1. Game Loop

- Updates game state (bird position, pipe movement).
- Renders frames (draw bird, pipes, score).
- Handles user input (tap or spacebar to flap).

### 2. Player (Bird)

- Constant gravity pulls the bird down.
- Pressing the space bar makes the bird flap upward.
- Collision detection with pipes, ground and ceiling.

### 3. Pipes

- Pairs of top and bottom pipes with a gap.
- Move leftward continuously.
- Randomized vertical position of the gap.
- New pipes spawn off-screen to the right.

### 4. Scoring

- Score increases when the bird passes the center a pipe pair.
- High score tracking (local storage: `high_score.json`).

### 5. Physics

- Gravity: pulls bird down each frame.
- Flap: applies an upward velocity.
- Velocity + gravity = realistic falling/flying effect.

### 6. Graphics

- Background: randomize background image.
- Bird: animated sprite (wing flaps, bird tilt),\
  randomize bird image (color).
- Pipes: top and bottom, identical shape,\
  randomize pipe image (color).
- Ground: scrolling to simulate movement.
- UI: score counter, game over screen.

### 7. Sound Effects

- Flap sound.
- Point scored sound.
- Collision sound.
- Die sound.

## 🛠️ Tools and Technologies

- Python (with pygame)

## 📦 Installation

```bash
git clone https://github.com/OrizWasTaken/flappy-bird-clone.git
cd flappy-bird-clone
pip install pygame
python main.py
```

## 🎨 Screenshots\*

![Gameplay Screenshot](./screenshots/gameplay.png)
_Add more screenshots or animated GIFs here._

---

## 🔧 Configuration\*

You can customize:

- Bird gravity & jump strength
- Pipe gap size
- Game speed
- etcetera

These settings can be found in `settings.py`.

---

## 📁 Project Structure\*

```
flappy-bird/
├── flappy_bird.py
├── bird.py
├── pipe.py
├── background.py
├── settings.py
├── game_stats.py
├── scoreboard.py
├── sound.py
├── gameover.py
├── README.md
├── assets/
|    -favicon.ico
│    -audio/
|    -backgrounds/
|    -bases/
|    -birds/
|    -gameover/
|    -medals/
|    -numbers/
|    -pipes/
```

---

## 🧠 Learnings

- Game loop mechanics
- Collision detection
- Sprite animation
- Procedural level generation
- Basic physics simulation

---

## 📜 License

MIT License — feel free to use and modify.

---

## 🙏 Credits\*

- Inspired by the original Flappy Bird by .Gears

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🧑‍💻 Author

Created by Joseph Orisakwe\
Email: oriz4work@gmail.com\
GitHub: https://github.com/OrizWasTaken
