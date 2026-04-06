import os
from pathlib import PurePath
from bag import Bag
import constants as const

from selenium import webdriver

with Bag() as bag:
    bag.load_page()
    print("Exiting ...")
