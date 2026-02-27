import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import BROWSER, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT


@pytest.fixture(scope="function")
def driver():

    if BROWSER.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    else:
        raise Exception("Browser not supported")

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

    yield driver

    driver.quit()