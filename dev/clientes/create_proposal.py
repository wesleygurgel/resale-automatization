import time

from models import Driver, Perguntas
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = Driver().get_driver()
    perguntas = Perguntas()
    driver.get('https://dev.resale.com.br/busca')
    time.sleep(5)
    imoveis = driver.find_elements(By.XPATH, '//a[contains(@href, "imovel")]')

    # Escolher Tipo de Venda
    # tipo_venda = perguntas.listar_imoveis_tipo()

    print(imoveis)

    for imovel in imoveis:
        if "venda direta" in imovel.accessible_name.lower():
            href = imovel.get_attribute('href')
            # open tab
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            # You can use (Keys.CONTROL + 't') on other OSs

            # Load a page
            driver.get('http://stackoverflow.com/')
            # Make the tests...

            # close the tab
            # (Keys.CONTROL + 'w') on other OSs.
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

    time.sleep(30)
