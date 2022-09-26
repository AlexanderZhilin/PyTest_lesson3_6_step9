from selenium.webdriver.common.by import By
import pytest
import time
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    time.sleep(5)

if __name__ == "__main__":
    pytest.main(['-s', '-v', '--browser_name=firefox', '--language=en', 'test_parser.py'])
