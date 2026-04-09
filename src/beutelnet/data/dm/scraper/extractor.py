import csv
from scraper import scrape_text

""" Create CSV from scraped data """
def create_csv(data:list[dict[str,str]], filename:str) -> None:

    if not data:
        print("No text input from html")
        return

    try:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    except Exception as e:
        print(f"Error writing CSV: {e}")
