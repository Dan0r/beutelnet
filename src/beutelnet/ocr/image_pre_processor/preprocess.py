from PIL import Image, ImageOps
from pathlib import Path
import os
from django.conf import settings

# Iterate over files in folder
class PreProcessor:

    """Takes images from directory, splits them and places them inside the specified directory"""
    def __init__(self, directory, new_directory):
        # Check if directory valid
        if not directory.is_dir():
            print("Path not found.")

        self.directory = directory 
        self.new_directory = new_directory

    """
    Main Preprocessor.
    Process the images in the following order:
    1. Crop images in storage/raw and place them into storage/preprocessed
    2. Apply grayscale to the already split images in storage/preprocessed
    """
    def preprocess(self):
        self._split_images()
        self._grayscale()

    """Split double column image into two single column images"""
    def _split_images(self):
        # Specify offset of the placement of the midpoint
        offset = -15 
        # Walk into image folder and split images
        counter = 0
        for path in settings.STORAGE_RAW_IMAGES_DIR.iterdir():
                print(f"Applying Greyscale and Crop: {path.name}")
                # Calculate image's bounding box and split at its midpoint 
                image = Image.open(path)
                width, height = image.size
                midpoint = width / 2 - offset

                # Crop left half of the imagePure path objects provide path-handling operations which don’t actually access a filesystem. There are three ways to access these classes, which we also call flavours:
                left_bbox = (0, 0, midpoint, height)
                left_crop = image.crop(left_bbox)
                # Join path to current-directory with filename and "-left"
                filename, ext = path.name.split(".")
                left_filename = f"{filename}-left.{ext}"

                path_left = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, left_filename)
                # path_left = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, "left-" + file)
                # Use PILLOW to save under this path
                left_crop.save(path_left, format="JPEG")

                # Crop right half of the image
                right_bbox = (midpoint, 0, width, height)
                right_crop = image.crop(right_bbox)
                # Join Path 
                filename, ext = path.name.split(".")
                right_filename = f"{filename}-right.{ext}"

                path_right = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, right_filename)
                right_crop.save(path_right, format="JPEG")

                counter += 2
        print(f"Images pre-processed: {counter}")

    """Grayscale images for better OCR results"""
    def _grayscale(self):
        for path in settings.STORAGE_PRE_PROCESSED_IMAGES_DIR.iterdir():
                image = Image.open(path)
                gray_image = ImageOps.grayscale(image)

                new_path = settings.STORAGE_PRE_PROCESSED_IMAGES_DIR / path.name
                gray_image.save(new_path, format="JPEG")


    def pre_process_images():
        image_processor = PreProcessor(settings.STORAGE_RAW_IMAGES_DIR, settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
        image_processor.preprocess()
