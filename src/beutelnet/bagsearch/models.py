from django.db import models
from django.conf import settings

from ocr.image_ocr.ocr_image import ProcessImage
from ocr.image_ocr.clean_ocr_output import ProcessOcr
from ocr.image_pre_processor.preprocess import PreProcessor

# Create your models here.
class VacuumBags(models.Model):
    supermarket = models.CharField(max_length=200)
    vacuum = models.CharField(max_length=200)
    size = models.CharField(max_length=200)

    def __str__(self):
        return f"Supermarkt: {self.supermarket}, Staubsauger-Modell: {self.vacuum}, Beutelgröße: {self.size}"

# Write function to fire off ocr module and make a commit with new images into the database

    """Push data through pipline. Commit to database."""
    @classmethod
    def push_new_data(cls):
        # 1. Preprocess the images in the raw directory
        image_processor = PreProcessor(settings.STORAGE_RAW_IMAGES_DIR, settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
        image_processor.preprocess()

        # 2. Recognises the text of all the, now pre-processed, images in the directory
        ocr_processor = ProcessImage(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
            # Return -> list[dict[str, str]]:
        ocrtext = ocr_processor.scan_dir()

        # 3. Push data into model
        for dictionary in ocrtext:
            vacuum = VacuumBags(supermarket=dictionary["supermarket"], vacuum=dictionary["vacuum"], size=dictionary["size"])
            vacuum.save()
