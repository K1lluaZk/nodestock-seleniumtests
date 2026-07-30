from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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
            
        self.btn_editar = (
            By.XPATH,
            ".//button[contains(text(),'Editar')]"    
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
    
    def editar_producto(self, nombre):

        fila = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'font-bold') and normalize-space(text())='{nombre}']/ancestor::div[contains(@class,'border')]"
                )
            )
        )


        boton_editar = fila.find_element(
            *self.btn_editar
        )

        boton_editar.click()


        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.nombre)
     )
        
    def obtener_nombre(self):

        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.nombre)
        )

        return campo.get_attribute("value")
    
    def borrar_producto_por_sku(self, sku):

        fila = (
            By.XPATH,
         f"//tr[.//td[contains(text(),'{sku}')]]"
        )

        elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(fila)
        )

        boton = elemento.find_element(
            By.XPATH,
            ".//button[contains(.,'Borrar')]"
        )

        boton.click()
        
    def aceptar_confirmacion(self):

        WebDriverWait(self.driver, 5).until(
            EC.alert_is_present()
        )

        self.driver.switch_to.alert.accept()

    def aceptar_confirmacion(self):

        WebDriverWait(self.driver, 5).until(
            EC.alert_is_present()
        )

        self.driver.switch_to.alert.accept()


    def cancelar_confirmacion(self):

        WebDriverWait(self.driver, 5).until(
            EC.alert_is_present()
        )

        self.driver.switch_to.alert.dismiss()


    def existe_producto(self, sku):

        elementos = self.driver.find_elements(
            By.XPATH,
            f"//td[contains(text(),'{sku}')]"
        )

        return len(elementos) > 0
    
    def buscar_producto(self, nombre):

        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "busqueda")
            )
        )

        campo.clear()
        campo.send_keys(nombre)
        
    def obtener_texto_busqueda(self):

        campo = self.driver.find_element(
            By.ID,
            "busqueda"
        )

        return campo.get_attribute("value")