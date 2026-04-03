


from selenium.webdriver.common.by import By

class XQAPage:

    def __init__(self, driver):
        self.driver = driver

    # 🔹 Locators (update based on actual UI)
    heading = (By.TAG_NAME, "h1")

    # 🔹 Actions
    def open_page(self, url):
        self.driver.get(url)

    def get_heading_text(self):
        return self.driver.find_element(*self.heading).text