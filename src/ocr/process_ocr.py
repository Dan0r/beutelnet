class ProcessOcr:

    @classmethod
    def clean_ocr_output(cls, strlist: list[str]) -> list[str]:
        text_anomalies = [ 
            "WEITERE",
            "JMALLFLRLR",
            "GEEIGNET",
            "(0)",
            "_ M&",
            "FOLGENDE",
            "MAX 4L",
            "S-BA"
            "STANDARD-BAG",
            "S-BA",
            "GREEN",
            "STANDARD",
            "POWER"
        ]
        # Remove whitespace, comma, specific words
        clean_strlist = [
            s for s in strlist
            if s.strip() and s.strip() != "," and len(s) > 3 and not any(t in s.upper() for t in text_anomalies)
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
