# Advent of Code

Playing around with [Advent of Code](https://adventofcode.com/)

[![language](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Setup

I use the following steps in Windows.

1. Install python: Install the latest Python 3 version from https://www.python.org/downloads
2. Install git and Git Bash: Install the latest git version from https://git-scm.com/downloads
3. Launch Git Bash to perform the remaining steps:
   1. git clone https://github.com/justinbeetle/advent_of_code.git
   2. cd advent_of_code
   3. python -m venv venv
   4. source venv/Scripts/activate
   5. pip install .
   6. (Optional) Save a session token from a browser cookie to token.txt: echo <session_token> > token.txt

Finding a session token in Chrome:
1. Navigate to [Advent of Code](https://adventofcode.com/) and log in
2. Launch developer tools: CTRL-SHIFT-I
3. Go to the Application tab
4. On the sidebar, navigate to Storage -> Cookies -> https://adventofcode.com/
5. Copy the value of the session key

## Running

Launch Git Bash and perform the following steps:
1. cd advent_of_code
2. source venv/Scripts/activate
3. Run any of the problem scripts: 2022/01/p1.py

## Quality Checking

Launch Git Bash and perform the following steps:
1. cd advent_of_code
2. source venv/Scripts/activate
3. pip install -r dev-requirements.txt
4. Run black: python -m black src 20*
5. Run mypy: python -m mypy src/aoc/aoc_solver_strategy.py --strict
6. Run pylint: python -m pylint $(git ls-files 'src/*.py')

