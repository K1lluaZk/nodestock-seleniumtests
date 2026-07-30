from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import time


def test_busqueda_producto_inexistente(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.ingresar_usuario("admin@gmail.com")
    login.ingresar_password("Mario123")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    productos = ProductsPage(driver)
    
    time.sleep(2)

    productos.buscar_producto("Producto_Inexistente_999999")
    
    WebDriverWait(driver, 2).until(
        lambda d: True
    )
    
    time.sleep(1)

    assert not productos.producto_existe("Producto_Inexistente_999999")