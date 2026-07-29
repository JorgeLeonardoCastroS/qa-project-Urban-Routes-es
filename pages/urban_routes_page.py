from data import data
from helpers.retrieve_code import retrieve_phone_code
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_number = data.phone_number
    boton_pedir_taxi = (By.XPATH, '//button[text()="Pedir un taxi"]')
    opcion_comfort = (By.XPATH,"//div[contains(@class, 'tcard')][.//div[contains(@class, 'tcard-title') and text()='Comfort']]",)
    opcion_flash = (By.XPATH, "//div[text()='flash']")
    cortina_acustica = ( By.XPATH, "//div[text()='Cortina acústica']")
    icono_taxi = (By.XPATH, "//div[text()='Taxi']")
    field_numero_de_telefono = (By.XPATH, "//div[text()='Número de teléfono']")
    phone_input = (By.XPATH, "//input[@id='phone']")
    campo_siguiente = (By.XPATH, "//button[@type='submit' and normalize-space(.)='Siguiente']")
    campo_codigo_de_telefono = (By.XPATH, "//input[@id='code']")
    campo_confirmar = (By.XPATH, "//button[text()='Confirmar']")
    metodo_de_pago = (By.XPATH, "//div[contains(@class, 'pp-text') and normalize-space(.)='Método de pago']")
    agregar_tarjeta = (By.XPATH, "//div[text()='Agregar tarjeta']")
    numero_de_tarjeta = (By.XPATH, "//input[@id='number']")
    campo_cvv = (By.XPATH,"//input[@id='code' and contains(@class, 'card-input')]")
    boton_agregar = (By.XPATH, "//button[@type='submit' and normalize-space(.)='Agregar']")
    boton_cerrar = (By.XPATH, "//div[contains(@class, 'payment-picker')]//div[@class='section active']//button[@class='close-button section-close']")
    elemento_chulito = (By.XPATH, "//label[@for='card-1']/span[@class='checkmark']")
    message_for_driver = (By.XPATH, "//input[@id='comment']")
    requisitos_del_pedido = (By.CSS_SELECTOR, ".r-sw-container .r-sw-label")
    boton_manta_y_panuelos = (By.XPATH, "//div[@class='switch']/span[contains(@class, 'slider')]")
    estado_boton_manta_y_panuelos = (By.XPATH, "//div[@class='switch']//input[@type='checkbox' and @class='switch-input']")
    agregar_helado = (By.XPATH, "//div[contains(@class, 'counter-plus') and normalize-space(.)='+']")
    contador_helado = (By.XPATH, "//div[contains(@class, 'r-counter-container') and .//div[text()='Helado']]//div[@class='counter-value']")
    pedir_un_taxi = (By.CSS_SELECTOR, "span.smart-button-main")
    modal_informacion_del_conductor = (By.CSS_SELECTOR, ".order-btn-group")
    modal_busqueda_taxi = (By.XPATH, "//div[contains(@class, 'order-header-title') and contains(text(), 'Buscar automóvil')]")
    informacion_conductor = (By.XPATH, "//div[@class='order-btn-group']/div[contains(@class, 'order-button')]/following-sibling::div[1]")
    numero_de_orden = (By.XPATH, "//div[contains(@class, 'order-number')]//div[contains(@class, 'number')]")
    calificacion_conductor = (By.CSS_SELECTOR, ".order-btn-rating")

    def __init__(self, driver):
        self.driver = driver

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.from_field).send_keys(address_from)
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def muestra_opcion_flash(self):
        return self.driver.find_element(*self.opcion_flash).is_displayed()
    def click_pedir_taxi(self):
        self.driver.find_element(*self.boton_pedir_taxi).click()

    def wait_for_option_comfort(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[contains(@class, 'tcard-title') and normalize-space(.)='Comfort']")))

    def seleccionar_opcion_comfort(self):
        elm=self.driver.find_element(*self.opcion_comfort)
        elm.click()
        mi_resultado = elm.get_attribute("class")
        return mi_resultado

    def muestra_icono_taxi(self):
        return self.driver.find_element(*self.icono_taxi).is_displayed()

    def click_field_numero_de_telefono(self):
        self.driver.find_element(*self.field_numero_de_telefono).click()

    def wait_for_modal_numero_de_telefono(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='phone']")))
    def set_campo_telefono(self):
        elm=self.driver.find_element(*self. phone_input)
        elm.send_keys(data.phone_number)
        numero_de_telefono = elm.get_attribute("value")
        return numero_de_telefono

    def click_campo_siguiente(self):
        self.driver.find_element(*self.campo_siguiente).click()

    def set_campo_codigo_de_telefono(self):
        self.driver.find_element(*self.campo_codigo_de_telefono).send_keys(retrieve_phone_code(self.driver))

    def click_campo_confirmar(self):
        self.driver.find_element(*self.campo_confirmar).click()

    def click_metodo_de_pago(self):
        self.driver.find_element(*self.metodo_de_pago).click()

    def wait_for_modal_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text()='Método de pago']")))

    def click_agregar_tarjeta(self):
        self.driver.find_element(*self.agregar_tarjeta).click()
    def set_numero_de_tarjeta(self):
        self.driver.find_element(*self.numero_de_tarjeta,).send_keys(data.card_number)

    def set_campo_cvv(self):
        self.driver.find_element(*self.campo_cvv).send_keys(data.card_code)

    def click_boton_agregar(self):
        self.driver.find_element(*self.boton_agregar).click()

    def wait_for_chulito(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[@for='card-1']/span[@class='checkmark']")))

    def tarjeta_agregada(self):
        elm=self.driver.find_element(*self.elemento_chulito)
        return elm.is_displayed()

    def click_boton_cerrar(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.boton_cerrar)).click()

    def set_message_for_driver(self):
        elm=self.driver.find_element(*self.message_for_driver)
        elm.send_keys(data.message_for_driver)
        informacion=elm.get_attribute("value")
        print(informacion)
        return informacion

    def click_requisitos_del_pedido(self):
        self.driver.find_element(*self.requisitos_del_pedido).click()

    def wait_for_manta_y_panuelos(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'r-type-switch')][.//div[text()='Manta y pañuelos']]//span[contains(@class, 'slider')]")))

    def click_boton_manta_y_panuelos(self):
        # 1. Haces clic en el slider visible
        self.driver.find_element(*self.boton_manta_y_panuelos).click()
        # 2. Retornas el estado real del checkbox (devuelve True o False)
        return self.driver.find_element(*self.estado_boton_manta_y_panuelos).is_selected()

    def click_agregar_helado(self):
        element=self.driver.find_element(*self.agregar_helado)
        ActionChains(self.driver).double_click(element).perform()
        return self.driver.find_element(*self.contador_helado).text

    def click_pedir_un_taxi(self):
        self.driver.find_element(*self.pedir_un_taxi).click()

    def wait_for_modal_informacion_del_conductor(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".order-btn-group")))
        return self.driver.find_element(*self.modal_busqueda_taxi).text

    def mostrar_informacion_del_conductor(self):
        conductor=WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.informacion_conductor))
        orden=WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.numero_de_orden))
        calificacion=WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(self.calificacion_conductor))
        print(conductor.text)
        print(orden.text)
        print(calificacion.text)