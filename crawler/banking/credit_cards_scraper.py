import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_credit_cards():
    urls = {
        "main": "https://www.paisabazaar.com/credit-card/",
        "comparison": "https://www.paisabazaar.com/credit-card/",
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
                "category": "credit_cards",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/banking/credit_cards_data.csv", all_data)

if __name__ == "__main__":
    scrape_credit_cards()
