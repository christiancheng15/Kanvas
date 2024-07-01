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

## Obtaining Tokens

1. Navigate to your Canvas instance and log in.
2. Open Developer Tools in your browser (usually by pressing F12 or right-clicking and selecting "Inspect").
3. In Developer Tools, go to the "Network" tab.
4. Reload the Canvas page to capture network requests.
5. Look for a network request (usually the first one) and click on it to view details.
6. In the request headers, find `_csrf_token` and `canvas_session`, under "Cookie" in "Request Headers"
7. Copy the values of `_csrf_token` and `canvas_session` for use in the scripts

## Like this project? 
If you find this project helpful or interesting, please consider starring it on GitHub and following [me](https://github.com/christiancheng15) for updates!