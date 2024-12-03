import re

# Read input from file
with open("input.txt", "r") as file:
    data = file.read()

def solve(input_data):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_data)
    
    result = sum(int(a) * int(b) for a, b in matches)
    return result

def solve2(input_data):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    mul_matches = list(re.finditer(mul_pattern, input_data))
    do_matches = list(re.finditer(do_pattern, input_data))
    dont_matches = list(re.finditer(dont_pattern, input_data))
    
    enabled = True
    total = 0
    
    for mul_match in mul_matches:
        mul_start = mul_match.start()
        
        last_do = None
        last_dont = None
        
        # Find nearest do() and don't() before this mul
        for do in do_matches:
            if do.start() < mul_start:
                last_do = do
            else:
                break
        for dont in dont_matches:
            if dont.start() < mul_start:
                last_dont = dont
            else:
                break
        
        # If there's a don't() before this mul, disable it
        if last_dont and (last_do is None or last_dont.start() > last_do.start()):
            enabled = False

        # If there's a do() before this mul, enable it
        elif last_do:
            enabled = True
        
        # If the mul is enabled, compute its result
        if enabled:
            a, b = mul_match.groups()
            total += int(a) * int(b)
    
    return total

if __name__ == "__main__":
    print("Part 1:", solve(data))
    print("Part 2:", solve2(data))
