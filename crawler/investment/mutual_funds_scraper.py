import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_mutual_funds():
    url = "https://scripbox.com/mutual-fund"  # ✅ Single URL
    all_data = []

    print(f"Scraping mutual funds from {url}")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[❌] Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

    for item in headings + paragraphs:
        if item.strip():
            all_data.append({
                "category": "mutual_funds",
                "subcategory": "main",  # ✅ Fixed since now there's only one page
                "content": item
            })

    save_data_to_csv("data/investment/mutual_funds_data.csv", all_data)
    print(f"[✔] Saved {len(all_data)} items to mutual_funds_data.csv")

if __name__ == "__main__":
    scrape_mutual_funds()
