import constants as const
from bag_filter import BagFilter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains

class Bag(webdriver.Chrome):

    def __init__(self, driver_path=const.DRIVER, options=None, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown

        if options is None:
            self.options = Options()
            self.options.add_experimental_option("detach", True)
            self.options.binary_location = const.BINARY
        else:
            self.options = options

        # Instantiates Webdriver
        service = Service(executable_path=driver_path)
        super(Bag, self).__init__(options=self.options, service=service)
     

    """ Accept cookie """
    def click_cookie(self):
        # Poll DOM for cookie button by executing Lambda every few milliseconds
        cookie_button = WebDriverWait(self, 5).until(
            # Select Shadow Host
            lambda d: d.find_element(By.CSS_SELECTOR, const.SHADOW_HOST)
                # Select Cookie iniside Shadow host
                # Important: Do all selections within the lambda
                      .shadow_root
                      .find_element(By.CSS_SELECTOR, const.COOKIE)
        )
        WebDriverWait(self,5).until(lambda d: cookie_button.is_displayed() and cookie_button.is_enabled())
        cookie_button.click()


    """ Close driver in context manager"""
    def __exit__(self, exec_type, exec_val, exec_tb):
        if self.teardown:
            self.quit()

    """ Load DM website """
    def load_page(self):
        self.get(const.URL)


    """ Open window that shows compatible models """
    def load_product_specs(self, product):
        # Wait for "Passende-Modelle"-Button to be clickable
        beutel_module = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, product))
        )

        beutel_module.click()


    """ Click 'Weitere Modelle' inside of the specifications """
    def load_further_specs(self):
        try:
            further_products = WebDriverWait(self, 10).until(
                presence_of_element_located((By.CSS_SELECTOR, const.FURTHER_PRODUCTS_BUTTON))
            )
            further_products.click()
        except Exception as e:
            print(f"Fehler beim Suchen nach dem Produkt: {e}")


    """ Return data in product specifications """
    def filter_products(self):
        filter = BagFilter(driver=self)
        filter.filter_products()

    """ Return vacuum bag size """
    def filter_size(self):
        filter = BagFilter(driver=self)
        filter.filter_size()
