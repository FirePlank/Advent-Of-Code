import os
import subprocess
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

session_cookie = os.getenv("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("SESSION_COOKIE not found in .env file")

def get_day_from_folder():
    """Get the day number from the current folder name."""

    folder_name = os.path.basename(os.getcwd())
    if folder_name.startswith("day"):
        return int(folder_name[3:])
    raise ValueError("Folder name must start with 'day' followed by the day number (e.g., day01)")

def run_solution():
    """Run the solution script and capture its output."""

    extensions = ["py", "cpp", "rs"]
    for ext in extensions:
        solution_file = f"solution.{ext}"
        if os.path.exists(solution_file):
            try:
                if ext == "py":
                    result = subprocess.run(["python", solution_file], capture_output=True, text=True)
                elif ext == "cpp":
                    executable = "./solution"
                    if not os.path.exists(executable):
                        # Compile C++ file
                        subprocess.run(["g++", solution_file, "-o", executable], check=True)
                    result = subprocess.run([executable], capture_output=True, text=True)
                elif ext == "rs":
                    executable = "./target/debug/solution"
                    if not os.path.exists(executable):
                        # Compile Rust file
                        subprocess.run(["cargo", "build"], check=True)
                    result = subprocess.run([executable], capture_output=True, text=True)
                else:
                    continue

                result_str = result.stdout.strip().replace("Part 1: ", "").replace("Part 2: ", "")
                return result_str
            
            except subprocess.CalledProcessError as e:
                raise RuntimeError(f"Error running solution file: {e}")
            
    raise FileNotFoundError("No solution file found in the folder")

def submit_answer(day, level, answer):
    """Submit the answer to Advent of Code."""

    url = f"https://adventofcode.com/2024/day/{day}/answer"
    headers = {"Cookie": f"session={session_cookie}"}
    data = {"level": level, "answer": answer}

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()

        if "That's the right answer" in response.text:
            print("Answer submitted successfully.")
        elif "That's not the right answer" in response.text:
            print("Incorrect answer. Please try again.")
        elif "You gave an answer too recently" in response.text:
            print("You submitted too quickly. Please wait before submitting another answer.")
        else:
            print("Failed to submit answer. Please check the response.")
            print(response.text)
    except requests.RequestException as e:
        print(f"Error submitting answer: {e}")

if __name__ == "__main__":
    level = input("Enter the level (1 or 2): ").strip()
    if not level.isdigit() or level not in ("1", "2"):
        print("Invalid level. Please enter 1 or 2.")
        exit()

    try:
        day = get_day_from_folder()
        answer = run_solution()
        print(f"Day {day}, Answer: {answer}")
        submit_answer(day, level, answer)
    except Exception as e:
        print(f"Error: {e}")
