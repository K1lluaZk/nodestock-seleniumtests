import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_consultar_producto(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.ingresar_usuario("admin@gmail.com")
    login.ingresar_password("Mario123")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    productos = ProductsPage(driver)

    timestamp = int(time.time())

    nombre_producto = f"Producto Selenium {timestamp}"

    productos.abrir_modal()

    productos.escribir_nombre(nombre_producto)

    productos.seleccionar_categoria("Electronica")

    productos.escribir_sku(f"SEL-{timestamp}")

    productos.escribir_precio("500")

    productos.escribir_stock("10")

    productos.guardar()

    productos.buscar_producto(nombre_producto)
    
    WebDriverWait(driver, 5).until(
        lambda d: productos.producto_existe(nombre_producto)
    )

    assert productos.producto_existe(nombre_producto)