import constants as const
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, driver):
        self.driver = driver
        
    def load(self):
        self.driver.get(const.URL)

    """ Accept cookie """
    def cookie(self):
        # Poll DOM for cookie button by executing Lambda every few milliseconds
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                # Select Shadow Host
                lambda d: d.find_element(By.CSS_SELECTOR, const.SHADOW_HOST)
                    # Select Cookie iniside Shadow host
                    # Important: Do all selections within the lambda
                          .shadow_root
                          .find_element(By.CSS_SELECTOR, const.COOKIE)
            )
            WebDriverWait(self.driver,5).until(lambda d: cookie_button.is_displayed() and cookie_button.is_enabled())
            cookie_button.click()
        except Exception as e:
            print(f"Fehler beim Klicken des Cookie: {e}")
