import csv
import json
import os

def convert_csv_to_json(csv_file, json_file):
    data = []
    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        with open(json_file, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"[✔] {csv_file} → {json_file}")
    except Exception as e:
        print(f"[✖] Failed to convert {csv_file}: {e}")
