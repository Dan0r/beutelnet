from PIL import Image
from pathlib import Path
import pytesseract
import os
from ocr.image_ocr.clean_ocr_output import ProcessOcr

class ProcessImage:
    """
    Static Settings for Tesseract: 
    psm 4: Assume a single column of text of variable sizes.
    """
    custom_psm_setting = '--psm 11'
    lang = 'deu'

    def __init__(self, directory, source=None, destination=None, image_path=None):
        self.directory = directory
        self.source = source
        self.destination = destination
        self.image_path = image_path

    def __repr__(self):
        return f"Image Path: {self.image_path}"
    
    def scan_image(self):
        string = pytesseract.image_to_string(Image.open(self.image_path), config=self.custom_psm_setting)
        return string.splitlines()

    """Retreive supermarket name and size from the image name"""
    def _parse_filename(self, image_path: str) -> tuple[str, str]:
        filename = os.path.basename(image_path)
        supermarket, bag = filename.split("-")[:2]
        return supermarket, bag


    """Extract text from image and clean data according to ProcessOcr module"""
    def _ocr_text(self, path: str) -> list[str]:
        text = pytesseract.image_to_string(
            Image.open(path),
            config=self.custom_psm_setting,
            lang=self.lang
        )
        text = text.splitlines()
        text = ProcessOcr.clean_ocr_output(text)
        return text

    """
    Scan directory for images
    Return dictionary{name of supermarket, name of vacuum model, size of vacuum bag}
    """
    def scan_dir(self) -> list[dict[str, str]]:
        result = [] 
        # path = Path(self.directory)

        for path in self.directory.iterdir():
                print(f"Processing: {path.name}")
                # Get supermarket name and size of the vacuum bag
                supermarket, size = self._parse_filename(path.name)
                text = self._ocr_text(path)

                # Push data into dictionary
                # vacuum = the vacuum-bag is compatible with the given vacuum name
                for vacuum in text: 
                    result.append({
                        "supermarket": supermarket,
                        "size": size,
                        "vacuum": vacuum 
                    })
        return result

    def output_ocrtext():
        ocr_processor = ProcessImage(STORAGE_PRE_PROCESSED_IMAGES_DIR)
        ocrtext = ocr_processor.scan_dir()
        return ocrtext
