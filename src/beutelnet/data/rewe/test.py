from bs4 import BeautifulSoup
import csv

""" Scrape text from REWE PDF on vaccum types """
def scrape_text() -> list[str]:
    text_anomalies = [
        "Modell",
        "Beutel-Nr."
    ]

    with open("staubsauger.html") as doc:
        soup = BeautifulSoup(doc, 'html.parser')

    output = []

    # Object
    current = {"supermarket": "REWE", "size": None, "vacuum": None}

    # track previous paragraph 
    # track current paragraph 
    # track next paragraph 

    # create a list
    # store previousprevious, previous current in list

    # List of three and then append in the end
    # Change state

    for paragraphs in soup.find_all('p'):
        for paragraph in paragraphs:
            print(paragraph)
        # prev_text = paragraph[index - 1].get_text().strip()
        # nex_text = paragraph[index + 1].get_text().strip()
        # 
        # Join products names that use → for concatenation rn 
        #     text = output["vacuum"][index - 1]

        # if cur_text == "→":
        #     cur_text = paragraph[index - 1] + "bis" + paragraph[index + 1]

        # Dont change state if string is empty brackets or PDF text anomaly
        if not cur_text or cur_text in text_anomalies or len(cur_text) < 3:
            continue

        # Change size, e.g. size="V05"
        if len(cur_text) == 3 and cur_text.startswith("V"):
            current["size"] = cur_text

            # If both fields filled, commit
            if current["vacuum"] is not None:
                output.append(current)
                # Reset state
                current = {"supermarket": "REWE", "size": None, "vacuum": None}

        # Change vacuum name. Ignore size=None to include headers
        else:
            if current["vacuum"] is not None:
                output.append(current)
                # Reset state
                current = {"supermarket": "REWE", "size": None, "vacuum": None}

            # Set next state
            current["vacuum"] = cur_text

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
