from itertools import combinations

with open("input.txt", "r") as file:
    data = file.read().splitlines()

antennas = [(x, y, c) for x, row in enumerate(data) for y, c in enumerate(row) if c != '.']

def solve(grid, include_lines=False):
    antinodes = set((x, y) for x, y, _ in antennas) if include_lines else set()

    for (x1, y1, c1), (x2, y2, c2) in combinations(antennas, 2):
        if c1 == c2:
            dx, dy = x2 - x1, y2 - y1
            if include_lines:
                for k in range(-50, 51):
                    antinodes.add((x1 + k * dx, y1 + k * dy))
            else:
                antinodes.add((x1 - dx, y1 - dy))
                antinodes.add((x2 + dx, y2 + dy))

    return len(antinodes.intersection({(x, y) for x in range(len(grid)) for y in range(len(grid[0]))}))

if __name__ == "__main__":
    print("Part 1:", solve(data, include_lines=False))
    print("Part 2:", solve(data, include_lines=True))
