import constants as const
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Bag(webdriver.Chrome):

    def __init__(self, driver_path=const.DRIVER, options=None, teardown=False):
        self.driver_path = driver_path
        self.options = Options().add_experimental_option("detach", True)
        self.teardown = teardown


        if options is None:
            self.options = Options()
            self.options.add_experimental_option("detach", True)
        else:
            self.options = options

        # Instantiates Webdriver
        super(Bag, self).__init__()
     

    """ Close driver in context manager"""
    def __exit__(self, exec_type, exec_val, exec_tb):
        if self.teardown:
            self.quit()


    def load_page(self):
        self.get(const.URL)
