with open("input.txt", "r") as file:
    data = file.read().splitlines()


def solve(input_data, allow_concat=False):
    total = 0
    for line in input_data:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        
        def backtrack(idx, current):
            if current > target:
                return False
            if idx == len(numbers):
                return current == target
            
            ops = [current * numbers[idx], current + numbers[idx]]
            if allow_concat:
                ops.append(int(str(current) + str(numbers[idx])))

            return any(backtrack(idx + 1, op) for op in ops)

        if backtrack(1, numbers[0]):
            total += target
    
    return total

if __name__ == "__main__":
    print("Part 1:", solve(data))
    print("Part 2:", solve(data, True))