import constants as const

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable,
)

class Bag(webdriver.Chrome):

    def __init__(self, driver_path=const.DRIVER, options=None, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown


        if options is None:
            self.options = Options()
            self.options.add_experimental_option("detach", True)
        else:
            self.options = options

        # Instantiates Webdriver
        super(Bag, self).__init__(options=self.options)
        self.maximize_window()
     
    """ Accept cookie """
    def click_cookie(self):
        # Wait for shadow host
        host = WebDriverWait(self, 10).until(
            presence_of_element_located((By.CSS_SELECTOR, const.SHADOW_HOST))
        )

        # Access shadow_root, that contains cookie button
        shadow_root = host.shadow_root

        # Poll DOM for cookie button by executing Lambda every few milliseconds
        cookie_button = WebDriverWait(self, 5).until(
            lambda _: shadow_root.find_element(By.CSS_SELECTOR, const.COOKIE)
            if shadow_root.find_element(By.CSS_SELECTOR, const.COOKIE).is_enabled()
            else False
        )

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
        beutel_module = self.find_element(By.CSS_SELECTOR, product)
        beutel_module.click()

    """ Click 'Weitere Modelle' inside of the specifications """
        
    def load_further_specs(self):
        try:
            further_products = WebDriverWait(self, 10).until(
                presence_of_element_located((By.CSS_SELECTOR, const.FURTHER_PRODUCTS_BUTTON))
            )
            further_products.click()
            print("didnt wrok")
        except Exception as e:
            print(f"Fehler beim Suchen nach dem Produkt: {e}")

    # """ Return data in product specifications """
    # # def scrape_product_specs(self)
