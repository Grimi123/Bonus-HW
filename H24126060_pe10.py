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
    global snake, food, special_food, direction, score, game_over, obstacles
    snake = [[10, 20], [10, 19], [10, 18]]
    food = [random.randint(1, 19), random.randint(1, 39)]
    special_food = [random.randint(1, 19), random.randint(1, 39)]
    direction = 'RIGHT'
    score = 0
    game_over = False
    obstacles = generate_obstacles()

# Function to generate obstacles
def generate_obstacles():
    obstacles = []
    max_obstacles = int(21 * 41 * 0.05)  # 5% of total cells
    num_obstacles = random.randint(1, max_obstacles)
    while len(obstacles) < num_obstacles:
        obstacle_length = random.randint(5, 10)
        is_vertical = random.choice([True, False])
        if is_vertical:
            row = random.randint(0, 21 - obstacle_length)
            col = random.randint(0, 39)
            obstacle = [[row + i, col] for i in range(obstacle_length)]
        else:
            row = random.randint(0, 19)
            col = random.randint(0, 41 - obstacle_length)
            obstacle = [[row, col + i] for i in range(obstacle_length)]
        # Ensure that the obstacle does not overlap with existing obstacles
        if not any(cell in obstacles for cell in obstacle):
            obstacles.extend(obstacle)
    return obstacles

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
            elif [i, j] in obstacles:
                print('▒', end='')  # Obstacles represented by inverted color cells
            else:
                print(' ', end='')
        print()

# Function to update the game state
def update_game():
    global snake, food, special_food, direction, score, game_over

    # Move the snake
    head = snake[0]
    if direction == 'UP':
        new_head = [(head[0] - 1) % 21, head[1]]
    elif direction == 'DOWN':
        new_head = [(head[0] + 1) % 21, head[1]]
    elif direction == 'LEFT':
        new_head = [head[0], (head[1] - 1) % 41]
    elif direction == 'RIGHT':
        new_head = [head[0], (head[1] + 1) % 41]

    # Check for collisions with obstacles
    if new_head in obstacles:
        game_over = True
        return

    # Check for collisions with snake's own body or screen boundary
    if new_head in snake:
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
    global direction, game_over, score, food, special_food
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
        elif key.upper() == ' ':
            input("Game paused. Press Enter to resume...")
        elif key.upper() == 'Q':
            game_over = True
        update_game()
        time.sleep(0.1)
    print('Game Over! Score:', score)
    print('Normal foods eaten:', score)
    print('Special foods eaten:', score)
    if any(x in snake for x in obstacles):
        print('Reason for game over: Collision with an obstacle')
    else:
        print('Reason for game over: Collision with itself')

# Main function
if __name__ == '__main__':
    initialize_game()
    play_game()
