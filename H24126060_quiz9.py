import random

def generate_path(maze, N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly.

    # your code here
    maze = {}
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = 0

    maze[(0, 0)] = 2
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
        maze[(r, c)] = 2
    return maze

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.
    
    # Count of obstacles added
    obstacles_added = 0
    
    # Loop until at least min_obstacles have been added
    while obstacles_added < min_obstacles:
        # Randomly select a cell
        row = random.randint(0, N - 1)
        col = random.randint(0, M - 1)
        
        # Check if the selected cell is empty and not part of the path
        if maze.get((row, col)) == 0:
            # Set obstacle at the selected cell
            try:
                maze[(row, col)] = 1
                obstacles_added += 1
            except KeyError:
                # Handle KeyError
                print("KeyError occurred while setting obstacle at cell ({}, {}). Skipping...".format(row, col))
    
    return maze
    
def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    while True:
        try:
            # Prompt user for input
            row = int(input("Enter row coordinate: "))
            col = int(input("Enter column coordinate: "))
            
            # Check if coordinates are within bounds
            if row < 0 or row >= N or col < 0 or col >= M:
                raise KeyError("Coordinates out of bounds")
            
            # Check if the cell is part of the path or already an obstacle
            if maze[(row, col)] == 2:
                print("Cannot set obstacle in a path cell.")
            elif maze[(row, col)] == 1:
                print("An obstacle is already present at this cell.")
            else:
                # Set obstacle at the specified cell
                maze[(row, col)] = 1
                break  # Exit loop if obstacle is successfully set
        except ValueError:
            print("Invalid input. Please enter integers for coordinates.")
        except KeyError as e:
            print(e)
    
    return maze
    
def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    while True:
        try:
            # Prompt user for input
            row = int(input("Enter row coordinate: "))
            col = int(input("Enter column coordinate: "))
            
            # Check if coordinates are within bounds
            if row < 0 or row >= N or col < 0 or col >= M:
                raise KeyError("Coordinates out of bounds")
            
            # Check if the cell is part of the path or already empty
            if maze[(row, col)] == 2:
                print("Cannot remove obstacle from a path cell.")
            elif maze[(row, col)] == 0:
                print("There is no obstacle at this cell.")
            else:
                # Remove obstacle at the specified cell
                maze[(row, col)] = 0
                break  # Exit loop if obstacle is successfully removed
        except ValueError:
            print("Invalid input. Please enter integers for coordinates.")
        except KeyError as e:
            print(e)
    
    return maze



def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells.

    # your code here
    print("+" + "---+" * M)
    for i in range(N):
        row_str = "|"
        for j in range(M):
            state = maze[(i, j)]
            if state == 0:    # Empty cell
                row_str += "   "
            elif state == 1:  # Obstacle
                row_str += " X "
            else:
                row_str += " O "    # Path cell
            row_str += "|"
        print(row_str)
        print("+" + "---+" * M)




def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    # load grid
    try:
        file_name = input("Enter the file name: ")
        with open(file_name, 'r') as file:
            line = file.readline().strip()
            while line:
                if line.isdigit():
                    N, M = map(int, line.split())
                    if N <= 0 or M <= 0:
                        raise ValueError("Invalid maze dimensions")
                    break
                line = file.readline().strip()  # Skip non-numeric lines

            else:
                raise ValueError("No valid maze dimensions found in the file")

    except (IOError, ValueError) as e:
        print("Error occurred while reading maze dimensions:", e)
        return

    maze = generate_path({}, N, M)

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles: "))
            if min_obstacles < 0 or min_obstacles > N * M:
                raise ValueError("Invalid number of obstacles")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    maze = add_obstacles(maze, min_obstacles, N, M)

    while True:
        print("\nMenu:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Print maze")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            maze = set_obstacle(maze, N, M)
        elif choice == '2':
            maze = remove_obstacle(maze, N, M)
        elif choice == '3':
            print_maze(maze, N, M)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()


