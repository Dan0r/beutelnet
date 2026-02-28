import sqlite3
from ocr.process_ocr import ProcessOcr 
from ocr.process_image import ProcessImage

class DatabaseWriter:
    con = sqlite3.connect("database/staubsauger.db")
    image_dir = "/home/furukawa/programming/staub/src/images/cropped"


    @classmethod
    def commit(cls):
        cur = cls.con.cursor()




        print("Commited data.")


        c.execute("""CREATE TABLE bags (
            name text, 
            size text, 
            supermarket text
        )""")


    """Takes cleaned ocr output and transforms into tuples"""
    @classmethod
    def create_tuples(self):
        ProcessImage()

        takes 



dir = "/home/furukawa/programming/staub/src/images/cropped"
image = "/home/furukawa/programming/staub/src/images/cropped/E05-2-cropped.jpg"
scanner = ProcessImage(dir, image)
string = scanner.scan_image()
cleaned_string =  ProcessOcr.clean_ocr_output(string)
company_names = ProcessOcr.get_likely_companynames(cleaned_string)
print(company_names)

