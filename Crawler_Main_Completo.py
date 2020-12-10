# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import csv
import os


HOME_URL = "https://www.ambito.com/contenidos/dolar.html"

XPATH_DOLAR_TURISTA = '//div[@data-indice="/dolarturista"]//span[@class="value data-valor"]'
XPATH_DOLAR_BLUE_COMPRA = '//div[@data-indice="/dolar/informal"]//span[@class="value data-compra"]'
XPATH_DOLAR_BLUE_VENTA = '//div[@data-indice="/dolar/informal"]//span[@class="value data-venta"]'
XPATH_DOLAR_OFICIAL_COMPRA = '//div[@data-indice="/dolar/oficial"]//span[@class="value data-compra"]'
XPATH_DOLAR_OFICIAL_VENTA = '//div[@data-indice="/dolar/oficial"]//span[@class="value data-venta"]'


def CrearDiccionario():
    driver = webdriver.Chrome(executable_path=r"C:\Users\Souls\Desktop\chromedriver_win32\chromedriver.exe")
    driver.get(HOME_URL)
    time.sleep(10)
    driver.maximize_window()
    #hasta aqui puede ser un modulo de Crawler que al final devuelve driver


    dolar_turista = driver.find_element_by_xpath(XPATH_DOLAR_TURISTA)
    dolar_blue_compra = driver.find_element_by_xpath(XPATH_DOLAR_BLUE_COMPRA)
    dolar_blue_venta = driver.find_element_by_xpath(XPATH_DOLAR_BLUE_VENTA)
    dolar_oficial_compra = driver.find_element_by_xpath(XPATH_DOLAR_OFICIAL_COMPRA)
    dolar_oficial_venta = driver.find_element_by_xpath(XPATH_DOLAR_OFICIAL_VENTA)
    driver.maximize_window()
    today = time.strftime("%d-%m-%Y %H:%M:%S")

    mi_diccionario ={
        "Fecha" : today,
        "Dolar Turista": dolar_turista.text,
        "Dolar Blue Compra": dolar_blue_compra.text,
        "Dolar Blue Venta": dolar_blue_venta.text,
        "Dolar Oficial Compra": dolar_oficial_compra.text,
        "Dolar Oficial Venta": dolar_oficial_venta.text

         }
    driver.quit()
    return mi_diccionario
    #hasta aqui puede ser un modulo Scraping que devuelve mi_diccionario



def run():
    valores_diccionario = CrearDiccionario()

    file_name = "Dolar_El_Ambito.csv"
    with open('{}'.format(file_name), 'a+', newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=valores_diccionario.keys())
        if os.stat(file_name).st_size == 0:
            writer.writeheader()

        writer.writerow(valores_diccionario)
    # hasta aqui se pude hacer un modulo saver que recive diccionarios

if __name__ == '__main__':
    run()
