from pathlib import PurePath
import time
from browser import Browser
from page import Page
from grid import Grid
import constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By

with Browser() as driver:
    page = Page(driver)
    page.load()
    page.cookie()


    product_grid = driver.find_element(By.CSS_SELECTOR, const.PRODUCT_GRID)

    grid = Grid(driver, product_grid)
    tiles = grid.get_tiles()

    for tile in tiles:
        tile.click()
        tile.exit()

#     bag.load_page()
#     bag.click_cookie()
#     bag.click_products()
#
#     # bag.load_product_specs(const.PRODUCT_BUTTON)
#     # bag.load_further_specs()
#     # bag.filter_size()
#     # bag.filter_products()
#     print("Exiting ...")
# # Iterate over product tiles, select their button
