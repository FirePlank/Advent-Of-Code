with open("input.txt", "r") as file:
    data = file.read().splitlines()

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
rows, cols = len(data), len(data[0])

def setup(grid):
    guard_pos = None
    facing = None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in directions:
                guard_pos = (r, c)
                facing = char
                break
        if guard_pos:
            break
    
    return guard_pos, facing

def solve(grid):
    visited = set()
    guard_pos, facing = setup(grid)

    while True:
        visited.add(guard_pos)
        dr, dc = directions[facing]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            facing = turns[facing]  # Turn right
        else:
            guard_pos = next_pos  # Move forward

    return len(visited)

def simulate(grid, obstruction, guard_pos, facing):
    visited_states = set()

    while True:
        state = (guard_pos, facing)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        dr, dc = directions[facing]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            return False

        if next_pos == obstruction or grid[next_pos[0]][next_pos[1]] == '#':
            facing = turns[facing]  # Turn right
        else:
            guard_pos = next_pos  # Move forward

def solve2(grid):
    guard_pos, facing = setup(grid)

    valid_positions = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != guard_pos:
                if simulate(grid, (r, c), guard_pos, facing):
                    valid_positions.add((r, c))

    return len(valid_positions)


if __name__ == "__main__":
    print("Part 1:", solve(data))
    print("Part 2:", solve2(data))