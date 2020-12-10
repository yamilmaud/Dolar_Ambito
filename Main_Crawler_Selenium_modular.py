import Modulo_Crawler
import Modulo_Scraper
import Modulo_Saver

HOME_URL = "https://www.ambito.com/contenidos/dolar.html"



def run():

    instancia_crawler = Modulo_Crawler.Crawler("chrome", headless=True)

    create_driver = instancia_crawler.create_driver()
    instancia_crawler.crawl(create_driver,HOME_URL)

    instancia_scraper = Modulo_Scraper.Scraper()
    valores_diccionario = instancia_scraper.CrearDiccionario(create_driver)
    create_driver.quit()

    file_name = "Dolar_El_Ambito.csv"
    instancia_saver = Modulo_Saver.Saver(file_name)
    instancia_saver.Crear_Csv(valores_diccionario)








if __name__ == '__main__':
    run()
