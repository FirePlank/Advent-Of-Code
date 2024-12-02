with open("input.txt", "r") as file:
    data = file.read().splitlines()

def solve(input_data):
    left = []
    right = []
    for line in input_data:
        l, r = line.split("   ")
        left.append(l)
        right.append(r)
    
    left.sort()
    right.sort()

    distance = 0
    for l, r in zip(left, right):
        distance += abs(int(l) - int(r))

    return distance

def solve2(input_data):
    left = []
    seen_right = {}

    for line in input_data:
        l, r = line.split("   ")
        left.append(l)

        if r in seen_right:
            seen_right[r] += 1
        else:
            seen_right[r] = 1

    similarity = 0
    for l in left:
        amount = seen_right.get(l, 0)
        similarity += int(l) * amount

    return similarity

if __name__ == "__main__":
    # print(solve(data))
    print(solve2(data))
