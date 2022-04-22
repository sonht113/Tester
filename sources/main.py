import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.techwithtim.net/")
        self.assertIn("Tech With Tim - Python & Java Programming Tutorials - techwithtim.net", driver.title)
        elem = driver.find_element(by=By.ID, value="menu-item-1571")
        elem.click()
        self.assertIn("Machine Learning With Python - TensorFlow & SkLearn -techwithtim.net", driver.title)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
