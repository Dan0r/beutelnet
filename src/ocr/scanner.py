from PIL import Image
import pytesseract
import os


class Scanner:
    """
    Static Settings for Tesseract: 
    psm 4: Assume a single column of text of variable sizes.
    """
    source = "/home/furukawa/programming/staub/src/images/images"
    destination = "/home/furukawa/programming/staub/src/images/cropped"

    custom_psm_setting = '--psm 4'
    lang = 'deu'

    def __init__(self, directory, image_path=None):
        self.directory = directory
        self.image_path= image_path

    def __repr__(self):
        return f"Image Path: {self.image_path}"

    
    def scan_image(self):
        string = pytesseract.image_to_string(Image.open(self.image_path), config=self.custom_psm_setting)
        return string.splitlines()

    def scan_dir(self):
        string = ""
        for roots, dirs, files in os.walk(self.directory):
            for file in files:
                string += pytesseract.image_to_string(Image.open(roots + "/" + file), config=self.custom_psm_setting, lang=self.lang)
        return string.splitlines()

# destination = "/home/furukawa/programming/staub/src/images/cropped"
# scanner = Scanner(destination, destination + "/E05-2-cropped.jpg")
# myList = scanner.scan_dir()
# print(myList)
