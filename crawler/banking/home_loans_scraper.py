import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_home_loans():
    urls = {
        "main": "https://www.paisabazaar.com/home-loan/",
        "comparison": "https://www.paisabazaar.com/home-loan/",
        "interest_rates": "https://www.paisabazaar.com/home-loan/interest-rates/",
        "eligibility": "https://www.paisabazaar.com/home-loan/eligibility-criteria/",
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
                "category": "home_loans",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/banking/home_loans_data.csv", all_data)

if __name__ == "__main__":
    scrape_home_loans()
