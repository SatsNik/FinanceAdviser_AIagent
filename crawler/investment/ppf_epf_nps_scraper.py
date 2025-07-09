import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_ppf_epf_nps():
    urls = {
        "main": "https://www.paisabazaar.com/investment-plans/",
        "ppf": "https://www.paisabazaar.com/public-provident-fund-ppf/",
        "epf": "https://www.paisabazaar.com/employee-provident-fund-epf/",
        "nps": "https://www.paisabazaar.com/national-pension-system-nps/",
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
                "category": "ppf_epf_nps",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/investment/ppf_epf_nps_data.csv", all_data)

if __name__ == "__main__":
    scrape_ppf_epf_nps()
