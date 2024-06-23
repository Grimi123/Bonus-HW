import random

def generate_path(N, M):
    maze = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        maze.append(row)

    maze[0][0] = 2
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
        maze[r][c] = 2
    return maze

def add_obstacles(maze, num_obstacles):
    path = []
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == 2:
                path.append((r, c))

    for _ in range(num_obstacles):
        while True:
            obstacle_row = random.randint(0, len(maze) - 1)
            obstacle_col = random.randint(0, len(maze[0]) - 1)
            if (obstacle_row, obstacle_col) in path:
                continue
            if maze[obstacle_row][obstacle_col] == "x":
                continue
            maze[obstacle_row][obstacle_col] = "x"
            break

    return maze

def generate_maze(N, M, num_obstacles):
    maze = generate_path(N, M)
    maze = add_obstacles(maze, num_obstacles)
    return maze

def print_maze(maze):
    print("+" + "---+" * len(maze[0]))
    for row in maze:
        row_str = "|"
        for val in row:
            if val == 0:
                row_str += "   "
            elif val == "x":
                row_str += " X "
            else:
                row_str += "   "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N * M - (N + M - 1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

maze = generate_maze(N, M, num_obstacles)
print("Generated Maze Map:")
print_maze(maze)
