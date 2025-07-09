import requests
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def scrape_health_insurance():
    urls = {
        "main": "https://www.policybazaar.com/health-insurance/",
        "individual": "https://www.policybazaar.com/health-insurance/individual-health-insurance-plans/",
        "family_floater": "https://www.policybazaar.com/health-insurance/family-floater-plans/",
        "critical_illness": "https://www.policybazaar.com/health-insurance/critical-illness-insurance/",
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
                "category": "health_insurance",
                "subcategory": category,
                "content": item
            })

    save_data_to_csv("data/insurance/health_insurance_data.csv", all_data)

if __name__ == "__main__":
    scrape_health_insurance()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from crawler.utils import save_data_to_csv

def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def scrape_health_insurance():
    urls = {
        "main": "https://www.policybazaar.com/health-insurance/",
        "individual": "https://www.policybazaar.com/health-insurance/individual-health-insurance-plans/",
        "family_floater": "https://www.policybazaar.com/health-insurance/family-floater-plans/",
        "critical_illness": "https://www.policybazaar.com/health-insurance/critical-illness-insurance/",
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
                "category": "health_insurance",
                "subcategory": category,
                "content": item
            })

    driver.quit()

    save_data_to_csv("data/insurance/health_insurance_data.csv", all_data)

if __name__ == "__main__":
    scrape_health_insurance()
