import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

service = Service(r"C:\Users\alexs\anaconda3\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#service= Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

caminho = r'''
https://www.hashtagtreinamentos.com/
'''
driver.get(caminho)

#time.sleep(5)
campo_nome = driver.find_element(By.ID, 'firstname').send_keys("Alex")
#time.sleep(5)
#campo_nome.send_keys("Alex")
#enviar = driver.find_element(By.CLASS_NAME, 'botao-formulario-newsletter').click()

time.sleep(15)

