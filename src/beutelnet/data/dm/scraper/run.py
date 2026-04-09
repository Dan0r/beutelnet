from pathlib import PurePath
import time
from browser import Browser
from page import Page
from productmodule import ProductModule 
import constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By

with Browser() as driver:
    page = Page(driver)
    page.load()
    page.cookie()


    product_module = driver.find_element(By.XPATH, const.PRODUCT_MODULE)

    grid = ProductModule(driver, product_module)
    tiles = grid.get_tiles()

    for tile in tiles:
        tile.expand()
        tile.load_further_specs()
        tile.filter_size()
        tile.filter_products()
        tile.exit()

