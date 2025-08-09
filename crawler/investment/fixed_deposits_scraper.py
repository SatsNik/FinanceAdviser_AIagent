import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_fixed_deposits():
    url = "https://scripbox.com/fixed-deposit"  # ✅ Single URL
    all_data = []

    print(f"Scraping fixed deposits from {url}")
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
        if item.strip():  # ✅ Skip empty strings
            all_data.append({
                "category": "fixed_deposits",
                "subcategory": "main",  # ✅ Only one category now
                "content": item
            })

    save_data_to_csv("data/investment/fixed_deposits_data.csv", all_data)
    print(f"[✔] Saved {len(all_data)} items to fixed_deposits_data.csv")

if __name__ == "__main__":
    scrape_fixed_deposits()
