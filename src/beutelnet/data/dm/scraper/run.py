import os
from pathlib import PurePath
from bag import Bag
import constants as const

from selenium import webdriver

product = 'button[data-dmid="fm-vcbf-product-footer-button"]'
with Bag() as bag:
    bag.load_page()
    bag.click_cookie()
    bag.load_product_specs(product)
    bag.load_further_specs()
    print("Exiting ...")

