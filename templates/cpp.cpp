#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string read_input(const string& filename) {
    ifstream input_file(filename);
    if (!input_file.is_open()) {
        throw runtime_error("Could not open input file");
    }
    string input((istreambuf_iterator<char>(input_file)),
                      istreambuf_iterator<char>());
    input_file.close();
    return input;
}

string solve(const string& data) {
    return "Solution Placeholder";
}

string solve2(const string& data) {
    return "Solution Placeholder";
}

int main() {
    try {
        string data = read_input("input.txt");
        cout << "Part 1: " << solve(data) << endl;
        cout << "Part 2: " << solve2(data) << endl;
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}