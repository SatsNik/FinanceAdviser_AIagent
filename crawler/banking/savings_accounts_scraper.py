import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_savings_accounts():
    urls = {
        "main": "https://www.bankbazaar.com/savings-account.html",
        "regular": "https://www.hdfcbank.com/personal/save/accounts/savings-accounts",
        "salary": "https://www.hdfcbank.com/personal/save/accounts/savings-accounts/types-of-savings-accounts",
        "zero_balance": "https://www.hdfcbank.com/personal/save/accounts/savings-accounts/types-of-savings-accounts",
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
                "category": "savings_accounts",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/banking/savings_accounts_data.csv", all_data)

if __name__ == "__main__":
    scrape_savings_accounts()
