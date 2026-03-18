from PIL import Image, ImageOps
import os
from django.conf import settings

# Iterate over files in folder
class PreProcessor:

    """Takes images from directory, splits them and places them inside the specified directory"""
    def __init__(self, directory, new_directory):
        # Check if directory valid
        if not os.path.isdir(directory):
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
        for root, dirs, files in os.walk(settings.STORAGE_RAW_IMAGES_DIR):
            for file in files:
                print(f"Preprocessing: {file}")
                file_path = settings.STORAGE_RAW_IMAGES_DIR / file
                # Calculate image's bounding box and split at its midpoint 
                image = Image.open(file_path)
                width, height = image.size
                midpoint = width / 2 - offset

                # Crop left half of the imagePure path objects provide path-handling operations which don’t actually access a filesystem. There are three ways to access these classes, which we also call flavours:
                left_bbox = (0, 0, midpoint, height)
                left_crop = image.crop(left_bbox)
                # Join path to current-directory with filename and "-left"
                path_left = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, "left-" + file)
                # Use PILLOW to save under this path
                left_crop.save(path_left, format="JPEG")

                # Crop right half of the image
                right_bbox = (midpoint, 0, width, height)
                right_crop = image.crop(right_bbox)
                # Join Path 
                path_right = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, "right-" + file)
                right_crop.save(path_right, format="JPEG")

                counter += 2
        print(f"Preprocessed images created: {counter}")

    """Grayscale images for better OCR results"""
    def _grayscale(self):
        for root, dirs, files in os.walk(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR):
            for file in files:
                image_path = os.path.join(root, file)
                image = Image.open(os.path.join(image_path))
                gray_image = ImageOps.grayscale(image)

                path = os.path.join(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR, file)
                gray_image.save(path, format="JPEG")


    def pre_process_images():
        image_processor = PreProcessor(settings.STORAGE_RAW_IMAGES_DIR, settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
        image_processor.preprocess()
