import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from crawler.utils import save_data_to_csv


def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver



def scrape_life_insurance():
    urls = {
        "main": "https://www.policybazaar.com/life-insurance/",
        "term_insurance": "https://www.policybazaar.com/life-insurance/term-insurance/",
        "endowment_policies": "https://www.policybazaar.com/life-insurance/endowment-plan/",
        "ulip_policies": "https://www.policybazaar.com/life-insurance/ulip-plans/",
    }

    all_data = []
    driver = get_browser()

    for category, url in urls.items():
        print(f"Scraping {category} from {url}")
        try:
            driver.get(url)
            time.sleep(5)  # Wait for page to load
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
            paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

            for item in headings + paragraphs:
                all_data.append({
                    "category": "life_insurance",
                    "subcategory": category,
                    "content": item
                })

            print(f"[✔] Scraped {len(headings) + len(paragraphs)} items from {url}")
        except Exception as e:
            print(f"[✖] Failed to scrape {category}: {e}")

    driver.quit()
    save_data_to_csv("data/insurance/life_insurance_data.csv", all_data)

if __name__ == "__main__":
    scrape_life_insurance()
