# Kanvas

Kanvas is a Python script designed to automate joining and leaving groups in Canvas using Canvas API. It utilizes Python's `requests` library for making HTTP requests and `multiprocessing.pool.ThreadPool` for concurrent operations.

## Features

- Automatic monitoring, joining, and leaving of groups in Canvas automatically.
- Utilizes Canvas API for group operations.
- Uses thread pool for concurrent group operations.

## Requirements

- Python 3.12

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/kanvas.git
cd kanvas
```

## Usage

1. Set up your Canvas API credentials and tokens in the script.
2. Customize `canvas_sessions` dictionary with Canvas session tokens.
3. Adjust `group_id` to the desired Canvas group ID.
4. Run the script: 
    - `python aio.py` (with monitoring)
    - `python bot.py` (without monitoring)

## Like this project?
If you find this project helpful or interesting, please consider starring it on GitHub and following [me](https://github.com/christiancheng15) for updates!