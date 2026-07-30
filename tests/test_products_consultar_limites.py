from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_busqueda_limite_50_caracteres(driver):

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

    texto = "A" * 100

    productos.buscar_producto(texto)

    valor = productos.obtener_texto_busqueda()

    assert len(valor) == 50