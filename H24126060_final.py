def matrix_input(prompt):
    while True:
        try:
            matrix_str = input(prompt)
            rows = matrix_str.strip().split('|')
            matrix = {}
            for i, row in enumerate(rows):
                elements = row.split(',')
                for j, elem in enumerate(elements):
                    matrix[(i, j)] = int(elem)
            return matrix
        except ValueError:
            print("Error: Please enter integers separated by commas and rows separated by '|'.")
        except Exception as e:
            print(f"An error occurred: {e}")

def matrix_multiply(U, V, n):
    M = {}
    
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U[(i, k)] * V[(k, j)] for k in range(n))
    
    return M

def print_matrix(M, n):
    print("M = U x V")
    for i in range(n):
        row = [M.get((i, j), 0) for j in range(n)]
        print(row)

def main():
    
    try:
        print("Enter matrix U:")
        U = matrix_input("U: ")
        
        print("Enter matrix V:")
        V = matrix_input("V: ")
        
        n = int(len(U) ** 0.5)  # Assuming U is a square matrix, calculate size n
        
        if len(U) != len(V) or n * n != len(U):
            print("Error: Matrices U and V must be of the same size and square matrices.")
            return
        
        M = matrix_multiply(U, V, n)
        
        print_matrix(M, n)
        
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
