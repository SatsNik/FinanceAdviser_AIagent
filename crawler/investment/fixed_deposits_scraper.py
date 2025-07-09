import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_fixed_deposits():
    urls = {
        "main": "https://www.paisabazaar.com/fixed-deposit/",
        "bank_fds": "https://www.paisabazaar.com/fixed-deposit/",
        "corporate_fds": "https://www.bajajfinserv.in/fixed-deposit",
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
                "category": "fixed_deposits",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/investment/fixed_deposits_data.csv", all_data)

if __name__ == "__main__":
    scrape_fixed_deposits()
