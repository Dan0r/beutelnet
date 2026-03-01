from src.images.image_pre_processor import PreProcessor 
from src.ocr.process_image import ProcessImage
from src.ocr.process_ocr import ProcessOcr

"""Where to load images from and where to place the processed images"""
image_directory =  "/home/furukawa/programming/staub/src/images/original/"
target_directory = "/home/furukawa/programming/staub/src/images/preprocessed/"

def pre_process_images():
    image_processor = PreProcessor(image_directory, target_directory)
    image_processor.preprocess()

if __name__ == '__main__':
    pre_process_images()
