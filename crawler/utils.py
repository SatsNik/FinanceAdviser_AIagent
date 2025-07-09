import csv
import os
import time
import json
import requests

# ------------------ Save to CSV ------------------
def save_data_to_csv(file_path, data, fieldnames=None):
    """
    Saves a list of dictionaries to a CSV file.

    Args:
        file_path (str): The full path to the CSV file.
        data (list): List of dictionaries containing the scraped data.
        fieldnames (list): Optional list of field names (columns) to write.
                           If not provided, it takes keys from the first data row.
    """

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Use fieldnames from first item if not explicitly provided
    if not fieldnames and data:
        fieldnames = data[0].keys()

    write_header = not os.path.exists(file_path)

    # Write data to CSV
    with open(file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file is newly created
        if write_header:
            writer.writeheader()

        writer.writerows(data)

    print(f"[✔] Saved {len(data)} rows to {file_path}")


# ------------------ Retryable HTTP Request ------------------
def get_response(url, headers=None, retries=3, timeout=10):
    """
    Makes an HTTP GET request with retries and timeout.

    Args:
        url (str): The URL to request.
        headers (dict): Optional HTTP headers.
        retries (int): Number of retry attempts on failure.
        timeout (int): Timeout for each request.

    Returns:
        requests.Response: The HTTP response object.

    Raises:
        Exception: If all retry attempts fail.
    """
    attempt = 0
    while attempt < retries:
        try:
            print(f"Requesting URL: {url}")
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            attempt += 1
            print(f"⚠️ Attempt {attempt} failed: {e}")
            time.sleep(2)  # Backoff before retrying

    raise Exception(f"❌ Failed to fetch URL after {retries} attempts: {url}")


# ------------------ CSV to JSON Converter ------------------
def convert_csv_to_json(csv_path, json_path):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_path (str): Path to the CSV file.
        json_path (str): Path where the JSON file will be saved.
    """
    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    with open(json_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"[✔] Converted {csv_path} → {json_path}")
