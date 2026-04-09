import constants as const
from tile import Tile

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ProductModule:

    """ Represents DM product module, that contains multiple products """
    def __init__(self, driver, product_grid:WebElement):
        self.driver = driver
        # Needs to be instantiated with XPATH to choose a specific module
        self.product_grid = product_grid 

    def get_tiles(self) -> list[Tile]:
        tiles = self.product_grid.find_elements(
            By.CSS_SELECTOR, const.PRODUCT_TILES
        )

        elements = []
        for tile in tiles:
            elements.append(Tile(self.driver, tile))

        return elements

    # """ After clicking on \"Passende Modelle \" this function returns 
    #     the box containing the product size, names, brands """
    # def get_specifications(self): 


    def click_all_tiles(self):
        for i in range(len(self.get_tiles())):
            tiles = self.get_tiles()  
            tiles[i].click()
