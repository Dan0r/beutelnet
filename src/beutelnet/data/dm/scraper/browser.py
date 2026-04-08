import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Browser:
    def __init__(self, driver_path=const.DRIVER, options=None, teardown=True):
        self.driver_path = driver_path
        self.teardown = teardown

        if options is None:
            self.options = Options()
            self.options.add_experimental_option("detach", True)
            self.options.binary_location = const.BINARY
        else:
            self.options = options

        self.driver = None

    """ Context Manager: Start Chrome Driver"""
    def __enter__(self):
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=self.options)
        return self.driver

    """ Context Manager: Exit Chrome Driver"""
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown and self.driver:
            self.driver.quit()
