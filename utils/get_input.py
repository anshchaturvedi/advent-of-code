from dotenv import load_dotenv
import requests
from datetime import datetime
import os

# Constants
load_dotenv()
AOC_YEAR = datetime.now().year
AOC_DAY = datetime.now().day 
AOC_SESSION_TOKEN = os.getenv("AOC_SESSION_TOKEN")


def make_get_request(year, day, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch input: {response.status_code}")


def get_puzzle_input(suppress_logs=False):
    try:
        puzzle_input = make_get_request(AOC_YEAR, AOC_DAY, AOC_SESSION_TOKEN)
        base_path = os.path.dirname(os.path.abspath(__file__))
        target_dir = os.path.join(base_path, f"../{AOC_YEAR}/day-{AOC_DAY:02}")
        os.makedirs(target_dir, exist_ok=True)
        target_file = os.path.join(target_dir, "full.txt")
        with open(target_file, "w") as file:
            file.write(puzzle_input)
        if not suppress_logs:
            print(f"Puzzle input for Day {AOC_DAY:02} saved to {target_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_puzzle_input()
