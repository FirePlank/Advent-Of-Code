import numpy as np

with open("input.txt", "r") as file:
    data = file.read().splitlines()

grid = np.array([list(row) for row in data])
rows, cols = grid.shape

def count_word(grid, word):
    count = 0
    directions = [
        (1, 0),  # Down
        (0, 1),  # Right
        (1, 1),  # Down-right
        (1, -1)  # Down-left
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(0 <= r + dr * i < rows and 0 <= c + dc * i < cols and 
                       grid[r + dr * i, c + dc * i] == word[i] for i in range(len(word))):
                    count += 1

    return count

def solve(grid):
    word = "XMAS"
    return count_word(grid, word) + count_word(grid, word[::-1])

def solve2(grid):
    count = 0
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            top_left, top_right = grid[i][j], grid[i][j + 2]
            bottom_left, bottom_right = grid[i + 2][j], grid[i + 2][j + 2]
            center = grid[i + 1][j + 1]

            if (
                center == 'A'
                and {top_left, top_right, bottom_left, bottom_right} == {'M', 'S'}
                and top_left != bottom_right
                and top_right != bottom_left
            ):
                count += 1

    return count

if __name__ == "__main__":
    print("Part 1:", solve(grid))
    print("Part 2:", solve2(data))

