def generate_pascals_triangle(rows):
    triangle = []
    
    # Base case: if only one row is requested, return [[1]]
    if rows == 1:
        return [[1]]
    
    # Recursively generate the previous rows
    prev_rows = generate_pascals_triangle(rows - 1)
    
    # Generate the current row based on the previous row
    current_row = [1]  # First element is always 1
    for i in range(1, rows - 1):
        current_row.append(prev_rows[rows - 2][i - 1] + prev_rows[rows - 2][i])
    current_row.append(1)  # Last element is always 1
    
    # Add the current row to the triangle
    triangle = prev_rows
    triangle.append(current_row)
    
    return triangle

def print_pascals_triangle(triangle, arrangement):
    max_width = len(" ".join(map(str, triangle[-1])))
    if arrangement == 'normal':
        for row in triangle:
            print(" ".join(map(str, row)).center(max_width))
    elif arrangement == 'reverse':
        for row in reversed(triangle):
            print(" ".join(map(str, row)).center(max_width))
    elif arrangement == 'left':
        for row in triangle:
            print(" ".join(map(str, row)).ljust(max_width))
    elif arrangement == 'right':
        for row in triangle:
            print(" ".join(map(str, row)).rjust(max_width))

def main():
    while True:
        rows_input = input("Enter the number of rows for Pascal's triangle: ")
        if not rows_input.isdigit() or int(rows_input) < 1:
            print("Please enter a positive integer greater than or equal to 1.")
        else:
            rows = int(rows_input)
            break
    
    while True:
        arrangement = input("Choose arrangement (normal, reverse, left, right): ")
        if arrangement not in ['normal', 'reverse', 'left', 'right']:
            print("Please choose one of the following arrangements: normal, reverse, left, right.")
        else:
            break

    triangle = generate_pascals_triangle(rows)
    print("\nPascal's Triangle:")
    print_pascals_triangle(triangle, arrangement)

if __name__ == "__main__":
    main()
