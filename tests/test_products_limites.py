from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_crear_producto_sin_sku(driver):

    driver.get("http://localhost:3000")

    login = LoginPage(driver)

    login.ingresar_usuario("admin@gmail.com")
    login.ingresar_password("Mario123")
    login.click_login()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )

    productos = ProductsPage(driver)

    productos.abrir_modal()
    
    productos.escribir_nombre(
        "Producto Limite Selenium"
    )

    productos.seleccionar_categoria(
        "Electronica"
    )

    productos.escribir_precio("100")

    productos.escribir_stock("5")

    productos.guardar()

    mensaje = productos.obtener_validacion_sku()

    assert mensaje != ""
    
    