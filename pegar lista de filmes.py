import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('--headless')
service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

caminho = r'''
https://www.ingresso.com/?city=aracaju&partnership=home'''


driver.get(caminho)
filmes = driver.find_elements(By.TAG_NAME,"img")
lista_filmes=[]
for filme in filmes:
    if filme.get_attribute('loading')=="lazy":
        capa_filme = filme.get_attribute('alt')
        if 'capa do filme' in capa_filme:
            nome_filme = capa_filme.replace('capa do filme','')
            if nome_filme in lista_filmes:
                pass
            else:
                lista_filmes.append(nome_filme)
for filme in lista_filmes:
    print(filme)
