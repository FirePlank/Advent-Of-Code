with open("input.txt", "r") as file:
        data = file.read()

files, free_space, file_id, pos = [], [], 0, 0
for idx, size in enumerate(map(int, data)):
    if idx % 2 == 0:
        files.append({"id": file_id, "size": size, "pos": pos})
        pos += size
        file_id += 1
    else:
        free_space.append({"size": size, "pos": pos})
        pos += size

def solve():
    blocks = [{"id": f["id"], "pos": f["pos"] + i} for f in files for i in range(f["size"])]
    empty_positions = [e["pos"] + i for e in free_space for i in range(e["size"])]
    
    blocks.reverse()
    for idx, empty_pos in enumerate(empty_positions):
        if idx < len(blocks) and blocks[idx]["pos"] > empty_pos:
            blocks[idx]["pos"] = empty_pos
    
    return sum(block["id"] * block["pos"] for block in blocks)

def solve2():
    files.sort(key=lambda x: -x["id"])
    free_space.sort(key=lambda x: x["pos"])
    
    for file in files:
        for idx, space in enumerate(free_space):
            if space["size"] >= file["size"] and space["pos"] < file["pos"]:
                file["pos"] = space["pos"]
                free_space[idx]["size"] -= file["size"]
                free_space[idx]["pos"] += file["size"]
                if free_space[idx]["size"] == 0:
                    free_space.pop(idx)
                break
    
    return sum(f["id"] * (f["pos"] + i) for f in files for i in range(f["size"]))

if __name__ == "__main__":
    print("Part 1:", solve())
    print("Part 2:", solve2())
