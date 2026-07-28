from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_password_incorrecto(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.ingresar_usuario("admin@gmail.com")
    login.ingresar_password("password_incorrecto")

    login.click_login()


    mensaje = login.obtener_mensaje_error()


    assert mensaje == "Error al iniciar sesión"

    assert "/dashboard" not in driver.current_url