from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Driver:
    def __init__(self):
        self.s = Service(GeckoDriverManager().install())

    def get_driver(self):
        driver = webdriver.Firefox(service=self.s)
        # driver.maximize_window()
        return driver


class Perguntas:

    def __init__(self):
        self.LISTA_IMOVEIS = {
            "1": "venda direta",
            "2": "venda judicial",
            "3": "disputa"
        }

    def validate_choice(self, validation_type, type):
        if validation_type == "tipo_venda":
            if type not in (1, 2, 3):
                print('\nPor favor escolha um valor que seja válido!')
                self.listar_imoveis_tipo()
                return False
            return True

    def listar_imoveis_tipo(self):
        print('============== Escolha qual tipo de Venda ==============')
        print('1- Venda Direta')
        print('2- Venda Judicial')
        print('3- Imóvel em Disputa')
        tipo_venda = int(input("Desejo imóvel que seja (1, 2 ou 3): "))
        if self.validate_choice("tipo_venda", tipo_venda):
            return self.LISTA_IMOVEIS[str(tipo_venda)]

    def tipo_imoveis(self):
        username = input("Enter username:")
