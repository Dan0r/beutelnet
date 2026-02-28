from PIL import Image
import os

# Iterate over files in folder
class Splitter:

    """Takes images from directory, splits them and places them inside the specified directory"""
    def __init__(self, directory, new_directory):
         self.directory = directory 
         self.new_directory = new_directory


    """Split double column image into two single column images"""
    def split_images(self):
        dir = self.directory 
        # Specify offset of the placement of the midpoint
        offset = -15 

        # Check if directory valid
        if os.path.isdir(dir):
            print("Path valid.")
        else:
            print("Path not found.")

        # Walk into image folder an split images
        counter = 0
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_path = self.directory + "/" + file
                # Calculate image's bounding box and split at its midpoint 
                image = Image.open(file_path)
                bbox = image.getbbox()
                midpoint = image.width / 2 - offset

                # Create new bounding box and crop
                temp = list(bbox)
                temp.pop(2)
                temp.insert(2, midpoint)
                new_bbox = tuple(temp)

                image_crop = image.crop(new_bbox)
                image_crop.save(self.new_directory + file.replace(".jpg", "") + "-cropped" + ".jpg")

                counter += 1
        print("Images cropped:" + str(counter) )
                



splitter = Splitter("/home/furukawa/programming/staub/ocr/ocr/src/ocr/images", "/home/furukawa/programming/staub/ocr/ocr/src/ocr/cropped/")

