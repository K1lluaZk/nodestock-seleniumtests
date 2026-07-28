from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_exitoso(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.ingresar_usuario("admin@gmail.com")
    login.ingresar_password("Mario123")

    login.click_login()


    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )


    assert "/dashboard" in driver.current_url