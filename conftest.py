import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import pytest
from datetime import datetime


@pytest.fixture
def driver():

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("capturas", exist_ok=True)

            nombre = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

            driver.save_screenshot(
                f"capturas/{nombre}"
            )