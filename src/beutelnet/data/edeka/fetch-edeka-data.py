from ocr.image_ocr.ocr_image import ProcessImage
from PIL import Image
import pathlib
from pathlib import Path
import csv

# Directory
ROOT = Path(__file__).parents[0]
PROCESSED_IMAGES_DIR = ROOT / "edeka" / "preprocessed"

""" Create CSV from currently loaded images """
def create_csv() -> None:
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

def main():
    create_csv()


if __name__ == '__main__':
    main()
