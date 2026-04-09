# Represents one product tile
import constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable,
)
from selenium.webdriver.remote.webelement import WebElement

class Tile:

    def __init__(self, driver, tile:WebElement):
        self.driver = driver
        self.tile = tile 

    """ Click the "Passende Modelle"-button """
    def expand(self):
        try:
            button = self._get_button()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((button))
            )
            button.click()

        except Exception as e:
            print(f"Fehler beim Laden von \"Passende Modelle \": {e}")


    """ Click "Weitere Modelle"-button inside of widget """
    def load_further_specs(self):
        try:
            buttons = self._get_furtherproducts()
            for button in buttons:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((button))
                )
                button.click()

        except Exception as e:
            print(f"Fehler beim Suchen nach dem Produkt: {e}")


    """ Click the exit button """
    def exit(self):
        try:
            button = self._get_exit_button() 
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((button))
            )
            button.click()

        except Exception as e:
            print(f"Exit button was not clicked {e}")

    """ Return vacuum bag size """
    def filter_size(self):
        try:
            # Element is in MODULE_CONTAINER but not TILE 
            heading = self.driver.find_element(By.CSS_SELECTOR, const.SIZE)

            size = heading.find_elements(By.TAG_NAME, "h2")

            for s in size:
                print(s.text.strip())

        except Exception as e:
            print(f"Fehler beim Filtern der Staubsaugerbeutel-Größe: {e}")

    """ Return product and brand names """
    def filter_products(self):
        try:
            ## In the DOM: product_name_box is child of ProductModule but not Tile
            product_name_box = self.driver.find_element(By.CSS_SELECTOR, const.PRODUCT_NAMES_BOX)
            elements = product_name_box.find_elements(By.CSS_SELECTOR, "p, h4, img")

            for element in elements:
                if element.tag_name == 'h4':
                    print(element.text.strip().upper())
                elif element.tag_name == 'img' and element.get_attribute('class') == const.BRAND_IMAGE:
                    print(element.get_attribute('alt').strip())
                elif element.tag_name == 'p':
                    print(element.text.strip())

        except Exception as e:
            print(f"Fehler beim Filtern der Produkt- und Herstellernamen: {e}")

    def _get_button(self):
        return self.tile.find_element(By.CSS_SELECTOR, const.PRODUCT_BUTTON)


    def _get_exit_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, const.CLOSE_BUTTON))
        )

    def _get_furtherproducts(self):
        try:
            buttons = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, const.FURTHER_PRODUCTS_BUTTON))
                )
            return buttons
        except Exception as e:
            print(f"Failed to click \"Weitere Modelle\": {e}")
