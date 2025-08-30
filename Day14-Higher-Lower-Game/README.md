# Project 14 : 🔼 Higher Lower Game 🔽
A simple console-based game where the player guesses which account has more followers.  
This project is built in **Python** and demonstrates the use of functions, loops, and randomization.

---

## 📌 Description
The Higher-Lower Game presents the player with two random accounts (e.g., celebrities, brands, or influencers) along with their descriptions and country.  
The player must guess which account has the higher follower count.  
If the guess is correct, the score increases and the game continues.  
If the guess is wrong, the game ends.

---

## 🎮 How It Works
1. Two random accounts are chosen from the dataset.
2. Player is shown:
   - **Name**
   - **Description**
   - **Country**
3. Player inputs their guess: `A` or `B`.
4. The program compares follower counts:
   - ✅ If correct → score +1, next round starts.
   - ❌ If wrong → game ends, final score is displayed.
5. The game keeps track of the current score until the player loses.

---

## ⚙️ Features
- Random selection of accounts for each round.
- Continuous play until a wrong guess is made.
- Score tracking.
- Simple and interactive console-based gameplay.
