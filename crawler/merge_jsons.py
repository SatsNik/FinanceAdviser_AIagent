import json

def merge_json_files(input_files, output_file):
    merged_data = []
    try:
        for file in input_files:
            with open(file, mode='r', encoding='utf-8') as f:
                data = json.load(f)
                merged_data.extend(data)

        with open(output_file, mode='w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=4, ensure_ascii=False)

        print(f"[✔] Merged into {output_file}")
    except Exception as e:
        print(f"[✖] Merge failed: {e}")
