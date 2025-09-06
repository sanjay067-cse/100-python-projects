# Project 17 : Quiz Game 🎮

This is a simple **True-or-False Quiz Game** built using **Object Oriented Programming (OOP)** in Python.  

The game lets you:  
- Play through a series of True/False questions
- Enter your answers interactively  
- Get instant feedback on whether you’re right or wrong  
- Keep track of your score as you play  

Example question:  

Q1: A slug's blood is green. (True/False)?  

You type your answer, and the game tells you if you’re correct and updates your score.  

---

## 🎯 Project Goal  
The purpose of this project was to practice creating and using classes in Python. Everything in the game — from the questions to the quiz logic — is handled using custom classes.  

---

## 📂 Project Structure  
- `question_model.py` → Defines the `Question` class  
- `quiz_brain.py` → Defines the `QuizBrain` class  
- `data.py` → Contains sample questions  
- `main.py` → Runs the quiz  

---

## 🛠️ How It Works  
1. The questions are stored as objects with text and answers.  
2. The **QuizBrain** class controls the game flow (asking questions, checking answers, tracking the score).  
3. The main file runs the game and interacts with the player.  



---

## ▶️ Example Gameplay  

Q1: A slug's blood is green. (True/False)?  
> True  
✅ Correct! Your score is: 1/1  

Q2: The sky is yellow. (True/False)?  
> False  
✅ Correct! Your score is: 2/2  
