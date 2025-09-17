# Project 23 : Turtle Crossing Game 🐢

A fun arcade-style game built with Python’s `turtle` graphics module.  
The player controls a turtle trying to cross the road while avoiding moving cars. With each successful crossing, the difficulty increases!

---

## 🎮 Features
- Turtle moves upward using the **Up Arrow**⬆️ key.
- Cars move horizontally across the screen.
- Each level increases car speed, making the game more challenging.
- GAME OVER when the turtle collides with a car.
- Simple and engaging gameplay loop.

---

## ✅ Rules of the Game
- Use only **Up Arrow** ⬆️ to move the turtle.  
- Avoid touching cars 🚗.  
- Reach the top safely to level up 🎯.  
- Collision = **Game Over** ☠️.  

---

## 📂 Project Structure
- `main.py` — Main game loop: Starts the game and handles game logic.  
- `player.py` — Defines the Player class (turtle movement & reset behavior).  
- `car_manager.py` — Defines the CarManager class (creates and moves cars, handles speed increase).  
- `scoreboard.py` — Defines the Scoreboard class (tracks and displays level, shows GAME OVER).  
