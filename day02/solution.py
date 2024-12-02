with open("input.txt", "r") as file:
    data = file.read().splitlines()

def is_safe(levels):
    decreasing = levels[0] > levels[1]
    
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if decreasing:
            if not (1 <= -diff <= 3):
                return False
        elif not (1 <= diff <= 3):
                return False
        
    return True

def solve(input_data):
    safe = 0
    for row in input_data:
        levels = list(map(int, row.split())) 

        if is_safe(levels):
            safe += 1

    return safe

def solve2(input_data):
    safe = 0
    for row in input_data:
        levels = list(map(int, row.split()))
        
        if is_safe(levels):
            safe += 1
            continue

        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            if is_safe(modified_levels):
                safe += 1
                break

    return safe

if __name__ == "__main__":
    # print(solve(data))
    print(solve2(data))
