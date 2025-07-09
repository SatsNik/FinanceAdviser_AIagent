from crawler.insurance import life_insurance_scraper, health_insurance_scraper, general_insurance_scraper, health_insurance_scraper
from crawler.investment import mutual_funds_scraper, fixed_deposits_scraper, ppf_epf_nps_scraper
from crawler.banking import savings_accounts_scraper, credit_cards_scraper, personal_loans_scraper, home_loans_scraper
from crawler.csv_to_json_converter import convert_csv_to_json
from crawler.merge_jsons import merge_json_files

# ------------------ Scraping ------------------
print("\n🔍 Running Scrapers")
life_insurance_scraper.scrape_life_insurance()
health_insurance_scraper.scrape_health_insurance()
general_insurance_scraper.scrape_general_insurance()

mutual_funds_scraper.scrape_mutual_funds()
fixed_deposits_scraper.scrape_fixed_deposits()
ppf_epf_nps_scraper.scrape_ppf_epf_nps()

savings_accounts_scraper.scrape_savings_accounts()
credit_cards_scraper.scrape_credit_cards()
personal_loans_scraper.scrape_personal_loans()
home_loans_scraper.scrape_home_loans()

# ------------------ CSV → JSON ------------------
print("\n🔁 Converting CSV to JSON")
convert_csv_to_json("data/insurance/life_insurance_data.csv", "data/insurance/insurance_knowledge_base.json")
convert_csv_to_json("data/insurance/health_insurance_data.csv", "data/insurance/insurance_knowledge_base.json")
convert_csv_to_json("data/insurance/general_insurance_data.csv", "data/insurance/insurance_knowledge_base.json")

convert_csv_to_json("data/investment/mutual_funds_data.csv", "data/investment/investment_knowledge_base.json")
convert_csv_to_json("data/investment/fixed_deposits_data.csv", "data/investment/investment_knowledge_base.json")
convert_csv_to_json("data/investment/ppf_epf_npf_data.csv", "data/investment/investment_knowledge_base.json")

convert_csv_to_json("data/banking/savings_accounts_data.csv", "data/banking/banking_knowledge_base.json")
convert_csv_to_json("data/banking/personal_loans_data.csv", "data/banking/banking_knowledge_base.json")
convert_csv_to_json("data/banking/home_loans_data.csv", "data/banking/banking_knowledge_base.json")
convert_csv_to_json("data/banking/credit_cards_data.csv", "data/banking/banking_knowledge_base.json")

# ------------------ Merging JSON ------------------
print("\n🔗 Merging JSON Files")
merge_json_files(
    [
        "data/insurance/insurance_knowledge_base.json",
        "data/investment/investment_knowledge_base.json",
        "data/banking/banking_knowledge_base.json"
    ],
    "data/final_knowledge_base.json"
)

print("\n✅ All tasks completed successfully!")
