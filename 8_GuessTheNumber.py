import random

Logo = """
   ___                   _____ _           _  _            _             
  / __|_  _ ___ ______  |_   _| |_  ___   | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-<    | | | ' \/ -_)  | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/    |_| |_||_\___|  |_|\_|\_,_|_|_|_|_.__/\___|_|  
                                                                         
"""
SELECTED_NUMBER = random.randint(1, 100)
LOW_DIFFICULTY_ATTEMPT = 10
HIGH_DIFFICULTY_ATTEMPT = 5


def correct_guess(n):
    """Return If Guess Is Correct"""
    global SELECTED_NUMBER
    if n < SELECTED_NUMBER:
        print("Too low")
        return False
    if n > SELECTED_NUMBER:
        print("Too high")
        return False
    if n == SELECTED_NUMBER:
        print("You are correct! ✨✨✨")
        return True


def set_difficulty():
    """Set the to either"""
    global HIGH_DIFFICULTY_ATTEMPT
    global LOW_DIFFICULTY_ATTEMPT
    difficulty = input("Choose a difficulty: [easy, hard]: ").lower()

    if difficulty == "easy":
        return LOW_DIFFICULTY_ATTEMPT
    if difficulty == "hard":
        return HIGH_DIFFICULTY_ATTEMPT


print(Logo)
attempts_left = set_difficulty()
while attempts_left > 0:
    guessed_number = int(input("Guess a number from 1-100: "))
    number_is_correct = correct_guess(guessed_number)
    if number_is_correct:
        print("you win!")
        break
    else:
        attempts_left -= 1
        if attempts_left <= 0:
            print(f"You lost 😢 the correct answer the {SELECTED_NUMBER}")
        else:
            print(f"You have {attempts_left} attempts left")
