# Project 22 : Pong Game

A classic Pong game recreated using Python's `turtle` graphics library.  
Two players can battle it out — control the paddles, hit the ball, and score points!  

---

## 🎮 Features
- Smooth paddle movement using keyboard controls.
- Ball bounces off walls and paddles with realistic physics.
- Scoreboard tracks left and right player points.
- Simple, retro-style gameplay — just like the original Pong!

---

## 🕹️ Controls
**Right Paddle (Player 1):**
- ⬆️ Arrow Key → Move Up  
- ⬇️ Arrow Key → Move Down  

**Left Paddle (Player 2):**
- **W** → Move Up  
- **S** → Move Down  

---

## 📏 Rules of the Game
1. The ball bounces off the top and bottom walls.  
2. If the ball hits a paddle, it bounces back.  
3. If the ball goes past the **right paddle**, the **left player** scores a point.  
4. If the ball goes past the **left paddle**, the **right player** scores a point.  
5. The scoreboard updates automatically as points are scored.  
6. Play continues until you decide to exit.  

---

## 📂 Project Structure
📁 Pong-Game  
 ┣ 📜 main.py         # Main game loop and setup  
 ┣ 📜 paddle.py       # Paddle class  
 ┣ 📜 ball.py         # Ball class  
 ┣ 📜 scoreboard.py   # Scoreboard class  
 ┗ 📜 README.md       # Project documentation  
