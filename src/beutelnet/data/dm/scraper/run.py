from pathlib import PurePath
import time
from browser import Browser
from page import Page
from grid import Grid
from tilefilter import TileFilter
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
        tile.expand()
        tile.load_further_specs()
        time.sleep(1)
        filter = TileFilter(driver, tile.tile)
        filter.filter_size()
        tile.exit()
