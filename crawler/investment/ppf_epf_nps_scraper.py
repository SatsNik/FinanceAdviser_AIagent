import os
import requests
import pandas as pd
from crawler.utils import save_data_to_csv

def scrape_ppf_epf_nps():
    csv_url = "https://www.kaggle.com/datasets/sachinpillai/employee-provident-fund-of-india/download?datasetVersionNumber=1"
    local_csv_path = "data/investment/ppf_epf_nps_data.csv"

    # Create directories if not exist
    os.makedirs(os.path.dirname(local_csv_path), exist_ok=True)

    print(f"Downloading EPF data from {csv_url} ...")
    try:
        response = requests.get(csv_url, stream=True)
        response.raise_for_status()

        with open(local_csv_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"[✔] CSV saved to {local_csv_path}")

    except requests.RequestException as e:
        print(f"[❌] Failed to download CSV: {e}")
        return

    # Optional: Read and re-save with additional metadata
    df = pd.read_csv(local_csv_path)
    df["category"] = "ppf_epf_nps"
    df["subcategory"] = "epf"

    save_data_to_csv(local_csv_path, df.to_dict(orient="records"))

if __name__ == "__main__":
    scrape_ppf_epf_nps()
