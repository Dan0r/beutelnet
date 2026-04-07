# Class responsible for extracting product resultsh
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

import constants as const


class BagFilter():
    def __init__(self, driver):
        self.driver = driver


    """ Return product names """
    def get_products(self):
        WebDriverWait(self.driver, 2)
        product_name_box = self.driver.find_element(By.CSS_SELECTOR, const.PRODUCT_NAMES_BOX)
        product_names = product_name_box.find_elements(By.TAG_NAME, "p")
        print(len(product_names))
