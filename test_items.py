from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    # time.sleep(30)
    assert WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")), "---!!! ADD TO CART BUTTON NOT FOUND !!!---")

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', '--browser_name=firefox', '--language=en', 'test_parser.py'])
