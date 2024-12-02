import os
import requests
from shutil import copyfile
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

session_cookie = os.getenv("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("SESSION_COOKIE not found in .env file")

def main():
    # Ask for the day
    day = input("Enter the day (1-25): ").strip()
    if not day.isdigit() or not (1 <= int(day) <= 25):
        print("Invalid day. Please enter a number between 1 and 25.")
        return
    day = int(day)
    
    # Create the folder
    day_folder = f"day{day:02d}"
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)
    
    # Download the input
    input_url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    try:
        response = requests.get(input_url, headers=headers)
        response.raise_for_status()
        input_data = response.text
        with open(os.path.join(day_folder, "input.txt"), "w") as input_file:
            input_file.write(input_data)
        print(f"Input for day {day} downloaded successfully.")
    except requests.RequestException as e:
        print(f"Error fetching input: {e}")
        return
    
    # Ask for the programming language
    lang = input("Which language template would you like to use? ").strip().lower()

    # Find the actual file with the extension
    for file in os.listdir("templates"):
        if file.startswith(f"{lang}."):
            template_file = os.path.join("templates", file)
            break
    else:
        raise FileNotFoundError(f"No template file found for language: {lang}")

    if not os.path.exists(template_file):
        print(f"No template found for '{lang}'.")
    else:
        ext = template_file.split('.')[-1]
        copyfile(template_file, os.path.join(day_folder, f"solution.{ext}"))
        print(f"Template for {lang} copied to {day_folder}/solution.{ext}.")
    
    # Copy the submit.py file
    submit_file = "submit.py"
    if os.path.exists(submit_file):
        copyfile(submit_file, os.path.join(day_folder, submit_file))
        print(f"submit.py copied to {day_folder}.")
    else:
        print("submit.py not found in the current directory.")

if __name__ == "__main__":
    main()
