# Number Guessing Game 🎯

A simple and interactive command-line game written in Python that simulates a number guessing game. The user has 8 attempts to guess a randomly generated number between 1 and 100, receiving hints after each incorrect guess. This project was developed to practice input validation, exception handling, and control flow logic in Python.

---

## Features

* **Dynamic Number Generation:** Uses Python's built-in `random` module to generate a new secret number between 1 and 100 every time a new game session starts.
* **Robust Input Validation:** Includes a `try-except` block to catch `ValueError` exceptions, ensuring the program doesn't crash if the user inputs non-integer characters.
* **Boundary Checking:** Features a custom validation check for numbers outside the 1-100 range, warning the player without penalizing their remaining attempts.
* **Interactive Feedback:** Implements dynamic conditional statements to guide the player by giving real-time hints ("Aim higher!" or "Aim lower!") based on their previous guess.

---

## How to use

1. Clone this repository:
   `git clone https://github.com/jerocubaque12/Number-Guess.git`
2. Run the script:
   `guessing_game.py`
3. Follow the on-screen instructions to pick your number and test your luck.

---

## Requirements

* Python 3.6+
* `random` module (built-in)

---

## Author

* Jeronimo Cubaque - https://github.com/jerocubaque12
