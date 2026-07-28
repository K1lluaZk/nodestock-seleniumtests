from selenium.webdriver.common.by import By
import time

from pages.login_page import LoginPage


def test_login_campos_vacios(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.click_login()

    time.sleep(3)


    username = driver.find_element(
        By.ID,
        "login-username"
    )

    password = driver.find_element(
        By.ID,
        "login-password"
    )


    print("Usuario:", username.get_attribute("validationMessage"))
    print("Password:", password.get_attribute("validationMessage"))


    assert username.get_attribute("validationMessage") != ""
    assert password.get_attribute("validationMessage") != ""