import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_RAW_DIR = os.path.join(ROOT_DIR, 'storage/')
STORAGE_RAW_IMAGES_DIR = os.path.join(STORAGE_RAW_DIR, 'raw/')
STORAGE_PRE_PROCESSED_IMAGES_DIR = os.path.join(STORAGE_RAW_DIR, 'preprocessed/')
DATABASE_PATH = os.path.join(STORAGE_RAW_DIR, 'database.db')
