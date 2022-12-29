""" Module defining the solve_problem template method """

from typing import Callable, Optional, TextIO

import os.path
import sys
import time
import urllib.request


def __download_file(url: str, session_token: Optional[str], filepath: str) -> None:
    """Download a file.

    :param url: Source URL of the file to be downloaded

    :param session_token: Cookie session token for user specific file

    :param filepath: Destination path for the file to be downloaded
    """
    print(f"Downloading {url} to {filepath}...", flush=True)
    try:
        opener = urllib.request.build_opener()
        if session_token is not None:
            opener.addheaders = [
                ("Cookie", f"session={session_token}"),
                ("User-Agent", "python-requests/2.19.1"),
            ]
        with opener.open(url) as resp, open(filepath, "wb") as file:
            file.write(resp.read())
    except urllib.error.HTTPError as http_error:
        print(f"WARN: Failed to download {url} with exception {http_error}", flush=True)


def __get_input_url(script_dir: str) -> str:
    """Determine the input file URL based on the path of the problem script directory.

    :param script_dir: Directory of the problem script

    :return: Input file URL based
    """
    year = os.path.basename(os.path.dirname(script_dir))
    day = int(os.path.basename(script_dir))
    return f"https://adventofcode.com/{year}/day/{day}/input"


def __get_session_token(script_dir: str) -> Optional[str]:
    """Read the value of the token.txt file at the base of the repo (uncontrolled)

    :param script_dir: Directory of the problem script

    :return: Contents of the token.txt file at the base of the repo, or None if it doesn't exist.
    """
    token_filepath = os.path.join(
        os.path.dirname((os.path.dirname(script_dir))), "token.txt"
    )
    if os.path.exists(token_filepath):
        with open(token_filepath, "r", encoding="utf-8") as file:
            return file.read().strip()
    else:
        print(
            f"WARN: File {token_filepath} does not exist.  Create it with a session token "
            f"pulled from an Advent of Code (https://adventofcode.com/) browser cookie to "
            f"enable downloading the input file",
            flush=True,
        )
    return None


def __download_input(script_dir: str, input_filepath: str) -> None:
    """Attempt to download the input.txt file if it doesn't exist

    :param script_dir: Directory of the problem script

    :param input_filepath: Filepath of the input.txt file
    """
    if not os.path.exists(input_filepath):
        __download_file(
            __get_input_url(script_dir), __get_session_token(script_dir), input_filepath
        )


def solve_problem(script: str, solve_problem_function: Callable[[TextIO], str]) -> None:
    """Method implementing a basic strategy for solving Advent of Code problems.

    Download the input if input.txt doesn't exist in the script directory.
    If test_input.txt and test_answer_p#.txt exist, test if the function on the test input.
    If input.txt exists and the test passed, print the answer obtained from input.txt.

    :param script: Calling script filepath

    :param solve_problem_function: Function to solve the problem from an input file
    """

    # Ensure the input.txt file is present
    script_dir = os.path.dirname(script)
    input_filepath = os.path.join(script_dir, "input.txt")
    test_input_filepath = os.path.join(script_dir, "test_input.txt")
    test_answer_filepath = os.path.join(
        script_dir, f"test_answer_{os.path.splitext(os.path.basename(script))[0].split('_')[0]}.txt"
    )
    __download_input(script_dir, input_filepath)

    if os.path.exists(test_input_filepath) and os.path.exists(test_answer_filepath):
        time_before_s = time.perf_counter()
        with open(test_input_filepath, "r", encoding="utf-8") as file:
            test_answer_actual = solve_problem_function(file)
        time_elapsed_s = time.perf_counter() - time_before_s

        with open(test_answer_filepath, "r", encoding="utf-8") as file:
            test_answer_expected = file.read().strip()

        is_success = test_answer_actual == test_answer_expected
        if is_success:
            prefix = "PASS: Test answer="
            conjunction = "matches expected="
        else:
            prefix = "FAIL: Test answer="
            conjunction = "does not match expected="

        is_multiline_answer = "\n" in test_answer_actual or "\n" in test_answer_expected
        if is_multiline_answer:
            print(
                f"{prefix}\n{test_answer_actual}\n     {conjunction}\n{test_answer_expected}",
                flush=True,
            )
        else:
            print(
                f"{prefix}{test_answer_actual} {conjunction}{test_answer_expected}",
                flush=True,
            )
        print(f"Time elapsed: {time_elapsed_s:0.6f} s", flush=True)

        if not is_success:
            sys.exit(1)
    else:
        if not os.path.exists(test_input_filepath):
            print(f"WARN: File {test_input_filepath} does not exist", flush=True)
        if not os.path.exists(test_answer_filepath):
            print(f"WARN: File {test_answer_filepath} does not exist", flush=True)

    if os.path.exists(input_filepath):
        time_before_s = time.perf_counter()
        with open(input_filepath, "r", encoding="utf-8") as file:
            answer = solve_problem_function(file)
        time_elapsed_s = time.perf_counter() - time_before_s

        is_multiline_answer = "\n" in answer
        if is_multiline_answer:
            print(f"\nAnswer=\n{answer}", flush=True)
        else:
            print(f"\nAnswer= {answer}", flush=True)
        print(f"Time elapsed: {time_elapsed_s:0.6f} s", flush=True)
    else:
        sys.exit(f"ERROR: File {input_filepath} does not exist")
