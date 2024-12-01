use std::fs;

fn read_input(filename: &str) -> String {
    fs::read_to_string(filename).expect("Could not read input file")
}

fn main() {
    let data = read_input("input.txt");
    // Replace this with the actual solution logic
    println!("Solution Placeholder");
}
