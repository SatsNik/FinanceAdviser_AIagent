import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_mutual_funds():
    urls = {
        "main": "https://groww.in/mutual-funds",
        "equity": "https://groww.in/mutual-funds/equity",
        "debt": "https://groww.in/mutual-funds/debt",
        "hybrid": "https://groww.in/mutual-funds/hybrid",
    }
    all_data = []

    for category, url in urls.items():
        print(f"Scraping {category} from {url}")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')

        headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        for item in headings + paragraphs:
            all_data.append({
                "category": "mutual_funds",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/investment/mutual_funds_data.csv", all_data)

if __name__ == "__main__":
    scrape_mutual_funds()
