use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Could not read input file")
}

fn solve(input: Vec<&str>) -> i32 {
    0
}

fn solve2(input: Vec<&str>) -> i32 {
    0
}

fn main() {
    let input: Vec<&str> = read_input("input.txt").lines().collect();

    println!("Part 1: {}", solve(input.clone()));
    println!("Part 2: {}", solve2(input.clone()));
}
