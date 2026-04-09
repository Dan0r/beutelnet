from bs4 import BeautifulSoup
import bs4
import csv


text_anomalies = [
    "Modell",
    "Beutel-Nr."
]


""" Scrape text from REWE PDF on vaccum types """
def scrape_text() -> list[str]:

    with open("staubsauger.html") as doc:
        soup = BeautifulSoup(doc, 'html.parser')

    output = []

    # Object
    current = {"supermarket": "REWE", "size": None, "vacuum": None}
    paragraphs = soup.find_all('p')

    i = 0
    while i < len(paragraphs):
        text = paragraphs[i].get_text(strip=True)

        # If there is an arrow, join previous two values and make it the new text 
        if i + 2 < len(paragraphs) and paragraphs[i + 2].get_text(strip=True) == "→":
            first = paragraphs[i].get_text(strip=True)
            second = paragraphs[i+1].get_text(strip=True)
            text = f"{first} bis {second}"

            i += 3

        else:
            i += 1

        # Keep state if text is empty, anomaly or arrow
        if not text or text in text_anomalies or len(text) < 3 and text != "→":
            continue

        # Change size
        if len(text) == 3 and text.startswith("V"):
            current["size"] = text 

        else:
            if current["vacuum"] is not None:
                output.append(current)

            # Reset
            current = {"supermarket": "REWE", "size": None, "vacuum": text}

    # If both fields filled, commit
    if current["vacuum"] is not None:
        output.append(current)

    return output

""" Create CSV from scraped data """
def create_csv() -> None:
    scrape_output = scrape_text()

    if not scrape_output:
        print("No text input from html")
        return

    try:
        with open("rewe.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=scrape_output[0].keys())
            writer.writeheader()
            writer.writerows(scrape_output)

    except Exception as e:
        print(f"Error writing CSV: {e}")

def main():
    create_csv()

if __name__ == '__main__':
    main()
