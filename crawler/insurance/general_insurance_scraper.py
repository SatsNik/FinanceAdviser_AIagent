from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # background me open hoga
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_general_insurance():
    urls = {
        "main": "https://www.policybazaar.com/general-insurance/",
        "motor": "https://www.acko.com/car-insurance",
        "home": "https://www.godigit.com/home-insurance",
        "travel": "https://www.godigit.com/travel-insurance",
    }

    all_data = []
    driver = get_browser()

    for category, url in urls.items():
        print(f"Scraping {category} from {url}")
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        headings = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]

        for item in headings + paragraphs:
            all_data.append({
                "category": "general_insurance",
                "subcategory": category,
                "content": item
            })

    driver.quit()

    save_data_to_csv("data/insurance/general_insurance_data.csv", all_data)

if __name__ == "__main__":
    scrape_general_insurance()
