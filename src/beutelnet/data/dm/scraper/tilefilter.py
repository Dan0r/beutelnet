# Class responsible for extracting product results
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import constants as const


from selenium.webdriver.remote.webelement import WebElement

class TileFilter():
    def __init__(self, driver, tile:WebElement):
        self.driver = driver
        self.tile = tile 

    """ Return vacuum bag size """
    def filter_size(self):
        try:
            heading = WebDriverWait(self.driver, 10).until(
                presence_of_element_located((By.CSS_SELECTOR, const.SIZE))
            )

            size = heading.find_elements(By.TAG_NAME, "h2")

            for s in size:
                print(s.text.strip())

        except Exception as e:
            print(f"Fehler beim Filtern der Staubsaugerbeutel-Größe: {e}")
    #
    # """ Return product and brand names """
    # def filter_products(self):
    #     try:
    #         product_name_box = self.driver.find_element(By.CSS_SELECTOR, const.PRODUCT_NAMES_BOX)
    #         elements = product_name_box.find_elements(By.CSS_SELECTOR, "p, h4, img")
    #
    #         for element in elements:
    #             if element.tag_name == 'h4':
    #                 print(element.text.strip().upper())
    #             elif element.tag_name == 'img' and element.get_attribute('class') == const.BRAND_IMAGE:
    #                 print(element.get_attribute('alt').strip())
    #             elif element.tag_name == 'p':
    #                 print(element.text.strip())
    #     except Exception as e:
    #         print(f"Fehler beim Filtern der Produkt- und Herstellernamen: {e}")
