"""get and print the status code of the response of a list of URLs from a .csv file."""

import requests
import csv
import logging
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "Task 2 - Intern.csv"
ERROR_FILE = BASE_DIR / "errors.txt"

logging.basicConfig(
    filename=ERROR_FILE,
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def get_urls_from_file(file_path: Path) -> list[str]:
    """get urls from a csv file."""
    urls = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row:
                urls.append(row[0])
    return urls


def get_status_code(url: str) -> Optional[int]:
    """get the status code of a url."""
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code
    except requests.exceptions.RequestException as err:
        logging.error(f"{url} -> {err}")
        return err


def main():
    """main function."""
    urls = get_urls_from_file(CSV_FILE)
    for url in urls:
        response = get_status_code(url)
        print(f"({response}) {url}\n")


if __name__ == "__main__":
    main()
