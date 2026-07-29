from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

        self.btn_nuevo_producto = (
            By.XPATH,
            "//button[contains(., 'Nuevo Producto')]"
        )

        
        self.modal_producto = (By.ID, "modalProducto")

        self.nombre = (By.ID, "prodName")
        self.categoria = (By.ID, "selectCategorias")
        self.sku = (By.ID, "prodSku")
        self.precio = (By.NAME, "price")
        self.stock = (By.ID, "prodStock")

        self.btn_guardar = (
            By.XPATH,
            "//button[contains(text(),'Guardar en Inventario')]"
        )

    def abrir_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_nuevo_producto)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.modal_producto)
        )

    def escribir_nombre(self, nombre):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.nombre)
        )
        campo.clear()
        campo.send_keys(nombre)

    def seleccionar_categoria(self, categoria):
        select = Select(
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.categoria)
            )
        )

        select.select_by_visible_text(categoria)

    def escribir_sku(self, sku):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.sku)
        )
        campo.clear()
        campo.send_keys(sku)

    def escribir_precio(self, precio):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.precio)
        )
        campo.clear()
        campo.send_keys(precio)

    def escribir_stock(self, stock):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.stock)
        )
        campo.clear()
        campo.send_keys(stock)

    def guardar(self):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_guardar)
        )
        
        boton.click()
        
        WebDriverWait(self.driver, 10).until(
        EC.url_contains("/dashboard")
    )
        


    def producto_existe(self, nombre):

        localizador = (
            By.XPATH,
            f"//div[contains(@class,'font-bold') and normalize-space(text())='{nombre}']"
        )

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(localizador)
            )
            return True
        except TimeoutException:
            return False
        
    def obtener_validacion_nombre(self):

        campo = self.driver.find_element(
            *self.nombre
        )

        return campo.get_attribute("validationMessage")
    
        mensaje = productos.obtener_validacion_nombre()

        assert mensaje != ""
        
    def obtener_validacion_sku(self):

        campo = self.driver.find_element(
            *self.sku
        )

        return campo.get_attribute("validationMessage")