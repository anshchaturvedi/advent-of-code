# Advent of Code configuration
from datetime import datetime
import os
import time
from dotenv import load_dotenv
import requests
import re
import pyperclip as pc


load_dotenv()
AOC_YEAR = datetime.now().year
AOC_DAY = datetime.now().day
AOC_SESSION_TOKEN = os.getenv("AOC_SESSION_TOKEN")
SUBMIT_URL = f"https://adventofcode.com/{AOC_YEAR}/day/{AOC_DAY}/answer"

dir4 = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def submit_solution(level, answer):
    """Submit the solution to Advent of Code."""
    headers = {
        "Cookie": f"session={AOC_SESSION_TOKEN}",
        "User-Agent": "advent_of_code_solution_script",
    }
    data = {"level": level, "answer": answer}
    response = requests.post(SUBMIT_URL, headers=headers, data=data)
    if response.status_code == 200:
        if "That's the right answer" in response.text:
            return True, "Correct! Solution submitted successfully."
        elif "That's not the right answer" in response.text:
            return False, "Incorrect answer. Please try again."
        elif "You don't seem to be solving the right level" in response.text:
            return False, "Already solved this level or wrong level."
        else:
            return False, "Unexpected response. Please check manually."
    else:
        return False, f"Submission failed with status code {response.status_code}."


def time_function(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = int(
        (end_time - start_time) * 1000
    )  # Convert to milliseconds and cast to int
    input_type = "sample" if "sample" in args[0] else "full"
    part = "part 1" if "part_1" in func.__name__ else "part 2"
    print(
        f"{input_type} input {part} took {elapsed_time} milliseconds and returned {result}"
    )
    if part == "part 2":
        pc.copy(result)

def nums(x):
    pattern = r"-?\d+"
    if isinstance(x, str):
        matches = re.findall(pattern, x)
        return list(map(int, matches))
    if isinstance(x, list):
        return nums("".join(x))

