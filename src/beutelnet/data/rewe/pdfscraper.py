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

    for i, paragraph in enumerate(paragraphs):
        text = paragraph.get_text(strip=True)

        # If there is an arrow, join previous two values and make it the new text 
        if text == "→" and i >= 2:
            previous_previous_value = paragraphs[i - 2].get_text(strip=True)
            previous_value = paragraphs[i - 1].get_text(strip=True)
            text = f"{previous_previous_value} bis {previous_value}"

        # Keep state if text is empty, anomaly or arrow
        if not text or text in text_anomalies or len(text) < 3 and text != "→":
            continue

        ## Change state

        # Change size
        if len(text) == 3 and text.startswith("V"):
            current_size = text 

            # If both fields filled, commit
            if current_vacuum:
                output.append({
                    "supermarket":"REWE",
                    "size": current_size,
                    "vacuum": current_vacuum
                })

        # Change vacuum name (if all other checks fail, current string is a vacuum name)
        else:
            current_vacuum = text 


        return output



""" Create CSV from currently loaded images """
def create_csv():
    ocr_processor = ProcessImage(PROCESSED_IMAGES_DIR)
    ocr_output = ocr_processor.scan_dir()

    if not ocr_output:
        print("No OCR output")
        return

    try:
        with open("data.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=ocr_output[0].keys())
            writer.writeheader()
            writer.writerows(ocr_output)

    except Exception as e:
        print(f"Error writing CSV{e}")

""" Create CSV from scraped data """
def create_csv() -> None:
    text = scrape_text()

    if not text:
        print("No text input from html")
        return
    
    try:
        with open("rewe.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=input)
            writer.writeheader()
            writer.writerows(text)

    except Exception as e:
        print(f"Error writing CSV: {e}")

def main():
    scrape_text()

if __name__ == '__main__':
    main()
