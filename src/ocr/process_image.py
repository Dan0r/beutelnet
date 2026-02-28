from PIL import Image
import pytesseract
import os

class ProcessImage:
    """
    Static Settings for Tesseract: 
    psm 4: Assume a single column of text of variable sizes.
    """
    source = "/home/furukawa/programming/staub/src/images/original"
    destination = "/home/furukawa/programming/staub/src/images/cropped"

    custom_psm_setting = '--psm 4'
    lang = 'deu'

    def __init__(self, image_directory, image_path=None):
        self.directory = image_directory
        self.image_path= image_path

    def __repr__(self):
        return f"Image Path: {self.image_path}"
    
    def scan_image(self):
        string = pytesseract.image_to_string(Image.open(self.image_path), config=self.custom_psm_setting)
        return string.splitlines()

    """Returns: [supermarket_name, bag_size, bag_names] """
    def scan_dir(self) -> list[str]:
        string = ""
        for roots, dirs, files in os.walk(self.directory):
            for file in files:
                supermarket_name = file.split("-")[0]
                bag_name = file.split("-")[1]
                print(supermarket_name, bag_name)

                path = os.path.join(roots, file)
                text = pytesseract.image_to_string(
                    Image.open(path),
                    config=self.custom_psm_setting,
                    lang=self.lang
                )
                string += text

        # Prepend supermarket and bag name
        return [supermarket_name, bag_name] + string.splitlines()

source = "/home/furukawa/programming/staub/src/images/original"
processor = ProcessImage(source)
bag_names = processor.scan_dir()
print(bag_names)



    ## Needs to return the size and supermarketname too
