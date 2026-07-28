from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_input = (By.ID, "login-username")
        self.password_input = (By.ID, "login-password")
        self.login_button = (
            By.XPATH,
            "//button[contains(text(),'Ingresar al sistema')]"
        )

    def ingresar_usuario(self, username):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )
        campo.clear()
        campo.send_keys(username)


    def ingresar_password(self, password):
        campo = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        )
        campo.clear()
        campo.send_keys(password)


    def click_login(self):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        boton.click()
        
    def obtener_mensaje_error(self):
        mensaje = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//span[contains(text(),'Error al iniciar sesión')]"
                )
            )
        )
        return mensaje.text
        
    