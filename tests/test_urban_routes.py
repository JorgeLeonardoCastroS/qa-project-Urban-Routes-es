from data import data
from pages.urban_routes_page import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_seleccionar_opcion_comfort(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        resultado = page.seleccionar_opcion_comfort()
        # Resultados esperados la opcion comfort queda activa
        assert "active" in resultado

    def test_rellenar_el_numero_de_telefono(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        resultado=page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        # Resultados esperados el campo recibió el número de telefono
        assert data.phone_number == resultado

    def test_agregar_una_tarjeta_de_credito(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.wait_for_chulito()
        resultado = page.tarjeta_agregada()
        page.click_boton_cerrar()
        assert resultado == True

    def test_message_for_driver(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.click_boton_cerrar()
        informacion = page.set_message_for_driver()
        assert data.message_for_driver == informacion

    def test_pedir_una_manta_y_panuelos(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.click_boton_cerrar()
        page.set_message_for_driver()
        page.click_requisitos_del_pedido()
        checkbox = page.click_boton_manta_y_panuelos()
        assert checkbox == True

    def test_pedir_dos_helados(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.click_boton_cerrar()
        page.set_message_for_driver()
        page.click_requisitos_del_pedido()
        page.wait_for_manta_y_panuelos()
        page.click_boton_manta_y_panuelos()
        contador = page.click_agregar_helado()
        assert contador == "2"

    def test_modal_para_buscar_un_taxi(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.click_boton_cerrar()
        page.set_message_for_driver()
        page.click_requisitos_del_pedido()
        page.wait_for_manta_y_panuelos()
        page.click_boton_manta_y_panuelos()
        page.click_agregar_helado()
        page.click_pedir_un_taxi()
        busqueda_taxi = page.wait_for_modal_informacion_del_conductor()
        assert busqueda_taxi == "Buscar automóvil"

    def test_informacion_del_conductor_en_el_modal(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.address_from)
        page.set_to(data.address_to)
        page.click_pedir_taxi()
        page.wait_for_option_comfort()
        page.seleccionar_opcion_comfort()
        page.click_field_numero_de_telefono()
        page.wait_for_modal_numero_de_telefono()
        page.set_campo_telefono()
        page.click_campo_siguiente()
        page.set_campo_codigo_de_telefono()
        page.click_campo_confirmar()
        page.click_metodo_de_pago()
        page.wait_for_modal_metodo_de_pago()
        page.click_agregar_tarjeta()
        page.set_numero_de_tarjeta()
        page.set_campo_cvv()
        page.click_boton_agregar()
        page.click_boton_cerrar()
        page.set_message_for_driver()
        page.click_requisitos_del_pedido()
        page.wait_for_manta_y_panuelos()
        page.click_boton_manta_y_panuelos()
        page.click_agregar_helado()
        page.click_pedir_un_taxi()
        page.wait_for_modal_informacion_del_conductor()
        page.mostrar_informacion_del_conductor()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()