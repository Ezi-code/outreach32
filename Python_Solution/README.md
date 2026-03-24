# URL Status Code Checker

## Problem
The task requires verifying the HTTP status codes of a large list of URLs provided in a CSV format. Manually checking hundreds of links is inefficient and error-prone.

## Solution
A Python script (`app.py`) that automates the process of reading URLs from a CSV file, performing HTTP GET requests, and reporting the status codes.

## How it Works
1. **CSV Parsing**: The script uses the `csv` module to read URLs from `Task 2 - Intern.csv`, skipping the initial header row.
2. **HTTP Requests**: It uses the `requests` library to fetch each URL.
3. **Optimizations**:
   - **Timeout**: A 5-second timeout is implemented to prevent the script from hanging on unresponsive servers.
   - **Error Handling**: Network failures or invalid URLs are caught and handled gracefully.
4. **Reporting**:
   - **Console Output**: Successful status codes (e.g., 200, 404, 403) are printed to the console in the format `(STATUS) URL`.
   - **Error Logging**: Critical errors (like connection timeouts or DNS failures) are logged to `error.txt` instead of cluttering the console, as per requirements.
5. **Robustness**: The script uses `isinstance(status, int)` to ensure it only prints valid HTTP status codes to the console.

## Usage
Run the script from the `/Python_Solution` directory:
```bash
python3 app.py
```
Check `errors.txt` for details on any failed requests.

### Testing
Run the test script from the `/Python_Solution` directory:
```bash
python3 -m unittest test.py
```
This will run the tests and print the results to the console.
