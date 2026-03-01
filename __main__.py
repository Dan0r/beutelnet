from src.images.image_pre_processor import PreProcessor 
from src.ocr.process_image import ProcessImage
from src.ocr.process_ocr import ProcessOcr

"""Specify directories to load and place images"""
image_directory =  "storage/original/"
target_directory = "storage/preprocessed/"


def pre_process_images():
    image_processor = PreProcessor(image_directory, target_directory)
    image_processor.preprocess()

def output_ocrtext():
    ocr_processor = ProcessImage(target_directory)
    ocrtext = ocr_processor.scan_dir()
    return ocrtext

def commit_to_database():
    return 1 

if __name__ == '__main__':
    pre_process_images()
