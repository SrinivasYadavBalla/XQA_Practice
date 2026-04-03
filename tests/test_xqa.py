import time
from pages.xqa_page import *
from utils.driver_factory import *
from config.config import *

def test_open_xqa_page():
    driver = get_driver()
    page = XQAPage(driver)
    config1 =ConfigReader()
    url = config1.get_base_url()
    assert url is not None
    page.open_page(url)
    time.sleep(10)
