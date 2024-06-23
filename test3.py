import random

def generate_maze(N, M):
    """
    Function to generate an empty maze.
    """
    maze = {(i, j): 0 for i in range(N) for j in range(M)}
    return maze

def add_obstacles(maze, min_obstacles, N, M):
    """
    Function to randomly add obstacles to the maze.
    """
    max_obstacles = N * M - 2
    if min_obstacles > max_obstacles:
        raise ValueError("Minimum number of obstacles exceeds maximum possible obstacles.")
    
    obstacles_added = 0
    while obstacles_added < min_obstacles:
        i = random.randint(0, N - 1)
        j = random.randint(0, M - 1)
        if maze[(i, j)] == 0:
            maze[(i, j)] = 1
            obstacles_added += 1

def set_obstacle(maze, N, M):
    """
    Function to manually set an obstacle in the maze.
    """
    try:
        i = int(input("Enter row index: "))
        j = int(input("Enter column index: "))
        if i < 0 or i >= N or j < 0 or j >= M:
            raise ValueError("Coordinates are out of bounds.")
        if maze[(i, j)] == 2:
            raise ValueError("Cannot set obstacle on path cell.")
        maze[(i, j)] = 1
        print("Obstacle set successfully.")
    except ValueError as ve:
        print(ve)

def remove_obstacle(maze, N, M):
    """
    Function to manually remove an obstacle from the maze.
    """
    try:
        i = int(input("Enter row index: "))
        j = int(input("Enter column index: "))
        if i < 0 or i >= N or j < 0 or j >= M:
            raise ValueError("Coordinates are out of bounds.")
        if maze[(i, j)] == 2:
            raise ValueError("Cannot remove obstacle from path cell.")
        maze[(i, j)] = 0
        print("Obstacle removed successfully.")
    except ValueError as ve:
        print(ve)

def print_maze(maze, N, M):
    """
    Function to print the current state of the maze.
    """
    for i in range(N):
        for j in range(M):
            if maze[(i, j)] == 0:
                print(' ', end=' ')
            elif maze[(i, j)] == 1:
                print('X', end=' ')
            elif maze[(i, j)] == 2:
                print('O', end=' ')
        print()

def main():
    """
    Main function to control the flow of the program.
    """
    try:
        filename = input("Enter the filename (grid78.txt or grid89.txt): ")
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        N, M = len(lines), len(lines[0].strip())
        maze = generate_maze(N, M)
        
        # Populate maze based on file contents
        for i in range(N):
            for j in range(M):
                if lines[i][j] == ' ':
                    maze[(i, j)] = 0
                else:
                    maze[(i, j)] = 1
        
        add_obstacles(maze, int(input("Enter the number of minimum obstacles: ")), N, M)
        
        # Add code to generate a random path from top-left to bottom-right
        
        while True:
            print("\nMenu:")
            print("1. Set obstacle")
            print("2. Remove obstacle")
            print("3. Print maze")
            print("4. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                set_obstacle(maze, N, M)
            elif choice == '2':
                remove_obstacle(maze, N, M)
            elif choice == '3':
                print_maze(maze, N, M)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
    except FileNotFoundError:
        print("File not found.")
    except ValueError as ve:
        print(ve)
    except KeyError:
        print("Invalid coordinates.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
