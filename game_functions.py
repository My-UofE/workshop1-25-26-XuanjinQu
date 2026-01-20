import random

# function to be used by game_1: Guess the Number
def pick_value(values):
    return values[len(values) // 2]


# function to be used in game_2: Higher or Lower
def check_higher_lower(current, next_num, guess):
    if (guess == 'h' and next_num > current) or (guess == 'l' and next_num < current):
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    found = False
    for i in range(len(word)):
        if word[i] == letter:  # 
            board[i] = letter   # 
            found = True
    if found :
        print(f"{letter}")
        return True
    else:
        print(f"{letter}")
        return False

