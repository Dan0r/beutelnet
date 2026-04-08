from pathlib import PurePath
import time
from bag import Bag
import constants as const

from selenium import webdriver

with Bag() as bag:
    bag.load_page()
    bag.click_cookie()
    bag.load_product_specs(const.PRODUCT_BUTTON)
    bag.load_further_specs()
    bag.filter_size()
    bag.filter_products()
    print("Exiting ...")
# Iterate over product tiles, select their button
