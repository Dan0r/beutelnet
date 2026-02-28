import sqlite3
from ocr.scanner import Scanner

class Writer:
    con = sqlite3.connect("database/staubsauger.db")
    image_dir = "/home/furukawa/programming/staub/src/images/cropped"


    @classmethod
    def clean_ocr_output(cls, strlist: list[str]) -> list[str]:
        text_anomalies = [ 
            "WEITERE",
            "JMALLFLRLR",
            "GEEIGNET",
            "(0)",
            "_ M&"
        ]
        # Remove whitespace, comma, specific words
        clean_strlist = [
            s for s in strlist
            if s.strip() and s.strip() != "," and not any(t in s.upper() for t in text_anomalies)
        ]
        return clean_strlist 
    
    """Retreives ALLCAPS characters from the box, usually used to declare the manufacturer of the vacuum bag"""
    @classmethod
    def get_likely_companynames(cls, strlist: list[str]) -> list[str]:
        company_names = list()
        for t in strlist:
            if t.isupper():
                company_names.append(t)
        return company_names

    @classmethod
    def commit(con):
        cur = con.cursor()


dir = "/home/furukawa/programming/staub/src/images/cropped"
image = "/home/furukawa/programming/staub/src/images/cropped/E05-2-cropped.jpg"
scanner = Scanner(dir, image)
string = scanner.scan_image()
cleaned_string =  Writer.clean_ocr_output(string)
company_names = Writer.get_likely_companynames(cleaned_string)
print(company_names)

