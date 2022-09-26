from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    check_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    # time.sleep(5)
    assert check_btn, "add to cart button not found"

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', '--browser_name=firefox', '--language=en', 'test_parser.py'])
