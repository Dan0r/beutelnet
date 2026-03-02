from src.images.image_pre_processor import PreProcessor 
from src.ocr.process_image import ProcessImage
from src.ocr.process_ocr import ProcessOcr
from src.data.databasewriter import DatabaseWriter

from config import STORAGE_RAW_DIR, STORAGE_RAW_IMAGES_DIR, STORAGE_PRE_PROCESSED_IMAGES_DIR, DATABASE_PATH

"""Specify directories to load and place images"""
def pre_process_images():
    image_processor = PreProcessor(STORAGE_RAW_IMAGES_DIR, STORAGE_PRE_PROCESSED_IMAGES_DIR)
    image_processor.preprocess()

def output_ocrtext():
    ocr_processor = ProcessImage(STORAGE_PRE_PROCESSED_IMAGES_DIR)
    ocrtext = ocr_processor.scan_dir()
    return ocrtext

def commit_new_table():
    writer = DatabaseWriter(DATABASE_PATH)
    writer.create_table()

def push_data_to_database():
    data = output_ocrtext()
    databasewriter = DatabaseWriter(DATABASE_PATH)
    databasewriter.push_data(data)

if __name__ == '__main__':
    push_data_to_database()
