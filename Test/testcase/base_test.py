import pathlib
import unittest
from selenium import webdriver
from data.data import Data
from selenium.webdriver.chrome.options import Options
from testconf.runconfiguration import headless, linux


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.data = Data
        options = Options()
        if headless:
            options.add_argument("--headless")
        if linux:
            self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver", options=options)
        else:
            self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver.exe", options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(3000)
        self.driver.get(self.data.base_url)

    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
