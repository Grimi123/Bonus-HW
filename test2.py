import random

def generate_path(N, M):
    maze = {}
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = "0"

    maze[(0, 0)] = "2"
    path = [(0, 0)]
    r, c = 0, 0
    while r != N - 1 or c != M - 1:
        if r == N - 1:
            c += 1
        elif c == M - 1:
            r += 1
        else:
            right_or_down = random.randint(0, 1)
            if right_or_down == 0:
                r += 1
            else:
                c += 1
        path.append((r, c))
        maze[(r, c)] = "2"
    return maze

def add_obstacles(maze, num_obstacles):
    path = [coord for coord, state in maze.items() if state == "2"]

    for _ in range(num_obstacles):
        while True:
            obstacle_coord = random.choice(list(maze.keys()))
            if obstacle_coord in path:
                continue
            if maze[obstacle_coord] == "1":
                continue
            maze[obstacle_coord] = "1"
            break

    return maze

def generate_maze(N, M, num_obstacles):
    maze = generate_path(N, M)
    maze = add_obstacles(maze, num_obstacles)
    return maze

def print_maze(maze, N, M):
    print("+" + "---+" * M)
    for i in range(N):
        row_str = "|"
        for j in range(M):
            state = maze[(i, j)]
            if state == "0":
                row_str += "   "
            elif state == "1":
                row_str += " X "
            else:
                row_str += " O "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * M)

N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N * M - (N + M - 1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

maze = generate_maze(N, M, num_obstacles)
print("Generated Maze Map:")
print_maze(maze, N, M)
