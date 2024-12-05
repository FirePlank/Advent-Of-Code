from collections import defaultdict, deque

with open("input.txt", "r") as file:
    data = file.read().splitlines()

def process_updates(input_data):
    rules = {}

    split_index = input_data.index("")
    rule_data = input_data[:split_index]
    update_data = input_data[split_index + 1:]

    for line in rule_data:
        val1, val2 = line.split("|")
        if rules.get(val1):
            rules[val1].append(val2)
        else:
            rules[val1] = [val2]

    valid_updates = []
    incorrect_updates = []

    for line in update_data:
        correct = True
        seen = {}
        for page in line.split(","):
            res = rules.get(page)
            if res:
                seen[page] = True
                for r in res:
                    if seen.get(r):
                        correct = False
                        incorrect_updates.append(line)
                        break

                if not correct:
                    break
        
        if correct:
            valid_updates.append(line)

    return valid_updates, incorrect_updates, rules

def solve(input_data):
    valid_updates, _, _ = process_updates(input_data)

    result = 0
    for entry in valid_updates:
        split = entry.split(",")
        result += int(split[len(split)//2])

    return result

def reorder_update(update, rules):
    update_nodes = update.split(",")
    subgraph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph for the update using the rules
    for parent in update_nodes:
        for child in rules.get(parent, []):
            if child in update_nodes:
                subgraph[parent].append(child)
                in_degree[child] += 1

    # Topologically sort the update nodes
    queue = deque([node for node in update_nodes if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)

        for neighbor in subgraph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update

def solve2(input_data):
    _, incorrect_updates, rules = process_updates(input_data)

    reordered_updates = []
    for update in incorrect_updates:
        reordered = reorder_update(update, rules)
        reordered_updates.append(reordered)

    result = 0
    for reordered in reordered_updates:
        result += int(reordered[len(reordered) // 2])

    return result

if __name__ == "__main__":
    print("Part 1:", solve(data))
    print("Part 2:", solve2(data))