from browser import Browser
from page import Page
from productmodule import ProductModule 
import constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By

""" Scrape supermarket name, size and vacuum name """
def scrape_text() -> list[dict[str,str]]:
    with Browser() as driver:
        page = Page(driver)
        page.load()
        page.cookie()


        product_module = driver.find_element(By.XPATH, const.PRODUCT_MODULE)

        grid = ProductModule(driver, product_module)
        tiles = grid.get_tiles()

        res = []

        for tile in tiles:
            tile.expand()
            tile.load_further_specs()
            size = tile.filter_size()
            vacuums = tile.filter_products()
            for vacuum in vacuums:
                res.append({
                    "supermarket":"DM",
                    "size": size,
                    "vacuum": vacuum
                })
            tile.exit()

    return res
