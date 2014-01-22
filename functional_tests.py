from selenium import webdriver
import unittest

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_get_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Hallelujah The Hills', self.browser.title)


if __name__ == '__main__':
    unittest.main()

