import os
import msvcrt
import random
import sys
import time

# Function to get keyboard input
def get_key():
    if msvcrt.kbhit():
        return msvcrt.getch().decode('utf-8')
    else:
        return ''

# Function to clear the screen
def clear_screen():
    os.system('cls')

# Function to initialize the game
def initialize_game():
    global snake, food, special_food, direction, score, game_over
    snake = [[10, 20], [10, 19], [10, 18]]
    food = [random.randint(1, 19), random.randint(1, 39)]
    special_food = [random.randint(1, 19), random.randint(1, 39)]
    direction = 'RIGHT'
    score = 0
    game_over = False

# Function to display the game board
def display_board():
    clear_screen()
    for i in range(21):
        for j in range(41):
            if [i, j] in snake:
                print('█', end='')
            elif [i, j] == food:
                print('π', end='')
            elif [i, j] == special_food:
                print('X', end='')
            else:
                print(' ', end='')
        print()

# Function to update the game state
def update_game():
    global snake, food, special_food, direction, score, game_over

    # Move the snake
    head = snake[0]
    if direction == 'UP':
        new_head = [head[0] - 1, head[1]]
    elif direction == 'DOWN':
        new_head = [head[0] + 1, head[1]]
    elif direction == 'LEFT':
        new_head = [head[0], head[1] - 1]
    elif direction == 'RIGHT':
        new_head = [head[0], head[1] + 1]

    # Check for collisions
    if new_head in snake or new_head[0] < 0 or new_head[0] >= 21 or new_head[1] < 0 or new_head[1] >= 41:
        game_over = True
        return

    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == food:
        score += 1
        food = [random.randint(1, 19), random.randint(1, 39)]
    else:
        snake.pop()

    # Check if snake eats special food
    if new_head == special_food:
        if len(snake) > 1:
            snake.pop()
        special_food = [random.randint(1, 19), random.randint(1, 39)]

# Function to play the game
def play_game():
    global direction, game_over
    while not game_over:
        display_board()
        key = get_key()
        if key.upper() == 'W':
            direction = 'UP'
        elif key.upper() == 'S':
            direction = 'DOWN'
        elif key.upper() == 'A':
            direction = 'LEFT'
        elif key.upper() == 'D':
            direction = 'RIGHT'
        elif key.upper() == 'Q':
            game_over = True
        update_game()
        time.sleep(0.1)

# Main function
if __name__ == '__main__':
    initialize_game()
    play_game()
    print('Game Over! Score:', score)